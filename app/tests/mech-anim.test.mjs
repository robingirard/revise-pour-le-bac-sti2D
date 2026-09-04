import { test } from 'node:test';
import assert from 'node:assert/strict';
import { K, toSvg, mul, translate, rotateAbout, apply, toAttr, poseAt, sliderPoint, IDENTITY, dashAt, DASH_PATTERN, rockerPoint } from '../js/mech-anim.js';

const close = (a, b, eps = 1e-6) => assert.ok(Math.abs(a - b) < eps, `${a} ≠ ${b}`);
const closePt = (p, q, eps = 1e-6) => { close(p[0], q[0], eps); close(p[1], q[1], eps); };

test('toSvg : boîte fixe, bord, axe y inversé', () => {
  const spec = { bbox: [-1, -2, 5, 3], border: 4 };
  closePt(toSvg([-1, 3], spec), [4, 4]);                 // coin haut-gauche → (bord, bord)
  closePt(toSvg([5, -2], spec), [4 + 6 * K, 4 + 5 * K]); // coin bas-droit
  closePt(toSvg([0, 0], spec), [4 + K, 4 + 3 * K]);
  closePt(toSvg([0, 0], { bbox: [0, 0, 1, 1] }), [4 + 0, 4 + K]); // bord par défaut : 4 pt
});

test('matrices : composition, translation, rotation trigonométrique à l’écran', () => {
  // rotateAbout(90°) : un point à droite du centre monte (y SVG diminue) = sens trigonométrique à l'écran
  closePt(apply(rotateAbout(90, 50, 50), [60, 50]), [50, 40]);
  closePt(apply(rotateAbout(180, 0, 0), [1, 0]), [-1, 0]);
  // mul(M, N) applique N puis M
  const M = mul(translate(10, 0), rotateAbout(90, 0, 0));
  closePt(apply(M, [1, 0]), [10, -1]);
  closePt(apply(IDENTITY, [3, 4]), [3, 4]);
  assert.equal(toAttr(translate(1.23456, -2)), 'matrix(1 0 0 1 1.2346 -2)');
});

test('poseAt : rotation continue, un quart de tour à t = 0,25', () => {
  const spec = { bbox: [0, 0, 4, 4], border: 0, classes: { E1: { motion: 'rotate', center: [2, 2], turns: 1 } } };
  const P = [3 * K, 2 * K];            // point à 1 cm à droite du centre (2,2)
  closePt(apply(poseAt(spec, 0).E1, P), P);
  closePt(apply(poseAt(spec, 0.25).E1, P), [2 * K, 1 * K]);   // au-dessus du centre : trigonométrique à l'écran
  closePt(apply(poseAt(spec, 0.5).E1, P), [1 * K, 2 * K]);
});

test('poseAt : translation en cm, direction y du dessin = y SVG négatif ; oscillation', () => {
  const spec = { bbox: [0, 0, 4, 4], border: 0, classes: { E: { motion: 'translate', dir: [0, 1], amplitude: 1, phase: 0 } } };
  closePt(apply(poseAt(spec, 0.25).E, [10, 10]), [10, 10 - K]);   // sin(π/2) = 1 → 1 cm vers le haut
  closePt(apply(poseAt(spec, 0.75).E, [10, 10]), [10, 10 + K]);
  // oscillation de ±90° autour du coin haut-gauche de la boîte (SVG (0,0)) : à t = 0,25, +90° trigonométrique
  const rock = { bbox: [0, 0, 4, 4], border: 0, classes: { E: { motion: 'rotate', center: [0, 4], amplitude: 90 } } };
  closePt(apply(poseAt(rock, 0.25).E, [10, 0]), [0, -10]);
  closePt(apply(poseAt(rock, 0.5).E, [10, 0]), [10, 0], 1e-6);
});

test('poseAt : bielle-manivelle — longueur de bielle conservée, piston sur sa droite', () => {
  const spec = { bbox: [-1.3, -1.6, 7.8, 2.3], border: 4, duration: 4, classes: {
    E0: { motion: 'fixed' },
    E1: { motion: 'rotate', center: [0, 0], turns: 1 },
    E2: { motion: 'coupler', crank: 'E1', a: [0.9, 1.5], slider: 'E3', b: [5, 0] },
    E3: { motion: 'slider', dir: [1, 0], coupler: 'E2' },
  } };
  const A0 = toSvg([0.9, 1.5], spec), B0 = toSvg([5, 0], spec), O = toSvg([0, 0], spec);
  const L = Math.hypot(B0[0] - A0[0], B0[1] - A0[1]);
  const r = Math.hypot(A0[0] - O[0], A0[1] - O[1]);
  for (const t of [0, 0.1, 0.25, 0.4, 0.5, 0.7, 0.9]) {
    const poses = poseAt(spec, t);
    assert.deepEqual(poses.E0, IDENTITY);
    const A = apply(poses.E1, A0), B = apply(poses.E3, B0);
    close(Math.hypot(A[0] - O[0], A[1] - O[1]), r, 1e-6);     // A reste sur le cercle de la manivelle
    close(B[1], B0[1], 1e-6);                                 // B reste sur l'axe du piston
    close(Math.hypot(B[0] - A[0], B[1] - A[1]), L, 1e-6);     // longueur de bielle conservée
    closePt(apply(poses.E2, A0), A, 1e-6);                    // la bielle suit A…
    closePt(apply(poses.E2, B0), B, 1e-6);                    // …et B
  }
  // à t = 0,5 la manivelle a fait un demi-tour : A est symétrique de A0 par rapport à O
  const half = apply(poseAt(spec, 0.5).E1, A0);
  closePt(half, [2 * O[0] - A0[0], 2 * O[1] - A0[1]], 1e-6);
});

test('poseAt : follow compose le mouvement suivi et le mouvement propre', () => {
  const spec = { bbox: [0, 0, 4, 4], border: 0, classes: {
    E3: { motion: 'translate', dir: [1, 0], amplitude: 1 },
    E2: { motion: 'follow', of: 'E3' },
    E4: { motion: 'follow', of: 'E3', then: { motion: 'translate', dir: [0, 1], amplitude: 1 } },
  } };
  const p = poseAt(spec, 0.25);
  closePt(apply(p.E2, [0, 0]), [K, 0]);
  closePt(apply(p.E4, [0, 0]), [K, -K]);
});

test('poseAt : un cycle de dépendances est détecté', () => {
  const spec = { bbox: [0, 0, 1, 1], classes: { A: { motion: 'follow', of: 'B' }, B: { motion: 'follow', of: 'A' } } };
  assert.throws(() => poseAt(spec, 0.1), /cycle/);
});

test('sliderPoint : solution la plus proche de B0, jamais NaN', () => {
  closePt(sliderPoint([0, 0], [4, 0], [1, 0], 5), [5, 0]);          // deux solutions ±5 : la plus proche de 4
  closePt(sliderPoint([0, 3], [4, 0], [1, 0], 5), [4, 0]);          // |AB0| = 5 déjà : B = B0
  const far = sliderPoint([0, 100], [4, 0], [1, 0], 5);             // hors d'atteinte : point le plus proche
  assert.ok(Number.isFinite(far[0]) && Number.isFinite(far[1]));
  closePt(far, [0, 0]);
});

test('dashAt : la courroie défile dans le sens du tracé et reboucle sur un nombre entier de motifs', () => {
  const spec = { bbox: [0, 0, 4, 4], border: 0, duration: 4, classes: { c: { motion: 'dash', speed: 29 } } };
  const P = DASH_PATTERN[0] + DASH_PATTERN[1];
  const d0 = dashAt(spec.classes.c, spec, 0), d1 = dashAt(spec.classes.c, spec, 1);
  assert.equal(d0.dasharray, DASH_PATTERN.join(' '));
  close(d0.dashoffset, 0);
  close(d1.dashoffset % P, 0);                       // un nombre entier de motifs par cycle : pas de saut
  assert.ok(dashAt(spec.classes.c, spec, 0.5).dashoffset < 0);   // décalage négatif = tirets vers l'avant
  close(d1.dashoffset, -Math.round((29 * 4) / P) * P);
  assert.equal(poseAt(spec, 0.3).c.a, 1);           // pas de transformation géométrique pour une courroie
});

test('rocker : quadrilatère articulé, le point B reste à distance r du pivot et L de A', () => {
  const spec = { bbox: [-1, -1, 7, 4], border: 0, classes: {
    E1: { motion: 'rotate', center: [0, 0], turns: 1 },
    E2: { motion: 'coupler', crank: 'E1', a: [0.8, 0], slider: 'E3', b: [4, 2.2] },
    E3: { motion: 'rocker', pivot: [4, 0], coupler: 'E2' } } };
  const A0 = toSvg([0.8, 0], spec), B0 = toSvg([4, 2.2], spec), D = toSvg([4, 0], spec);
  const L = Math.hypot(B0[0] - A0[0], B0[1] - A0[1]), r = 2.2 * K;
  for (const t of [0, 0.1, 0.3, 0.5, 0.7, 0.9]) {
    const poses = poseAt(spec, t);
    const A = apply(poses.E1, A0), B = apply(poses.E3, B0);
    close(Math.hypot(B[0] - D[0], B[1] - D[1]), r, 1e-6);            // le balancier tourne autour de D
    close(Math.hypot(B[0] - A[0], B[1] - A[1]), L, 1e-6);            // la bielle garde sa longueur
    closePt(apply(poses.E2, B0), B, 1e-6);                           // l'extrémité B de la bielle est sur le balancier
    closePt(apply(poses.E2, A0), A, 1e-6);                           // et son extrémité A sur la manivelle
  }
  closePt(apply(poseAt(spec, 0).E3, B0), B0);                        // position dessinée à t = 0
});

test('rockerPoint : intersection de deux cercles, côté choisi par l’orientation', () => {
  const B = rockerPoint([0, 0], [4, 0], 2, 3, 1);
  close(Math.hypot(B[0], B[1]), 3); close(Math.hypot(B[0] - 4, B[1]), 2);
  const B2 = rockerPoint([0, 0], [4, 0], 2, 3, -1);
  close(B2[1], -B[1]);                                               // solution symétrique
});

test('aim : le corps du vérin vise le point mobile, la tige y reste attachée (slide)', () => {
  const spec = { bbox: [0, 0, 8, 4], border: 0, classes: {
    E1: { motion: 'rotate', center: [5, 0.6], amplitude: -15, phase: 0.75, offset: -15 },   // benne : 0° → −30° (horaire : l'avant, à gauche de C, monte)
    E2: { motion: 'aim', pivot: [1.2, 0], at: 'E1', point: [2.6, 1.9] },
    E3: { motion: 'aim', pivot: [1.2, 0], at: 'E1', point: [2.6, 1.9], slide: true } } };
  const O = toSvg([1.2, 0], spec), P0 = toSvg([2.6, 1.9], spec);
  closePt(apply(poseAt(spec, 0).E1, P0), P0, 1e-6);                  // offset + amplitude·sin(2π·0.75) = 0° : au repos
  for (const t of [0.1, 0.25, 0.5]) {
    const poses = poseAt(spec, t);
    const P = apply(poses.E1, P0);
    closePt(apply(poses.E3, P0), P, 1e-6);                           // la tige suit l'attache sur la benne
    closePt(apply(poses.E2, O), O, 1e-6);                            // le corps pivote autour de O…
    const Q = apply(poses.E2, P0);                                   // …et sa direction vise P
    const ang = (a, b) => Math.atan2(a[1] - O[1], a[0] - O[0]) - Math.atan2(b[1] - O[1], b[0] - O[0]);
    close(ang(Q, P), 0, 1e-6);
  }
  const lifted = apply(poseAt(spec, 0.5).E1, P0);                    // à t = 0,5 : −30°, l'attache P (à gauche de C) est montée (y SVG plus petit)
  assert.ok(lifted[1] < P0[1]);
});
