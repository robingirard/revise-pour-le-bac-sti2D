// answers.js — vérification des réponses (fonctions pures, testables)

/** Égalité de deux ensembles (tableaux ou Set). */
export function setEquals(a, b) {
  const sa = new Set(a), sb = new Set(b);
  if (sa.size !== sb.size) return false;
  for (const x of sa) if (!sb.has(x)) return false;
  return true;
}

/** Normalisation d'une réponse texte : minuscules, sans accents, sans espaces, virgule → point. */
export function normalizeAnswer(s) {
  return String(s ?? '')
    .trim()
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/\s+/g, '')
    .replace(/,/g, '.');
}

/** Vérifie une réponse saisie pour un item de type `input`. */
export function checkInput(payload, value) {
  const given = normalizeAnswer(value);
  if (given === '') return false;
  if (payload.numeric) {
    const x = Number(given);
    const expected = Number(normalizeAnswer(payload.answer));
    if (Number.isNaN(x) || Number.isNaN(expected)) return false;
    return Math.abs(x - expected) <= (Number(payload.tolerance) || 0) + 1e-12;
  }
  const accepted = [payload.answer, ...(payload.accept || [])].map(normalizeAnswer);
  return accepted.includes(given);
}
