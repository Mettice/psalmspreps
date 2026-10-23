// Independent language-form checks used by the Form Three intensive generator.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { fr2Present, fr2With } from '../../../src/engine/lib/french2.js';

test('s’exclamer: compute regular endings and join the required reflexive pronoun', () => {
  const pronouns = ['m’', 't’', 's’', 's’', 'nous ', 'vous ', 's’', 's’'];
  const expected = ['je m’exclame', 'tu t’exclames', 'il s’exclame', 'elle s’exclame',
    'nous nous exclamons', 'vous vous exclamez', 'ils s’exclament', 'elles s’exclament'];
  assert.deepEqual(pronouns.map((r, p) => fr2With(p, r + fr2Present('exclamer', p))), expected);
});
