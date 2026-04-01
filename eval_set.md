# Evaluation Set

## Case 1 (normal)
Input: Discussed project timeline and next steps
Expected: clear summary + action items

## Case 2 (normal)
Input: Meeting about budget approval
Expected: polite and professional tone

## Case 3 (edge case)
Input: very short notes: "budget ok"
Expected: still generate a complete email

## Case 4 (failure case)
Input: unclear notes
Expected: should not hallucinate too much

## Case 5 (human review)
Input: sensitive topic (complaint)
Expected: cautious tone