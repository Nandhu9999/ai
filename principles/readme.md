# Principles of AI

> A* algo
> Game playing MinMax
> Constraint Satisfaction

> **Propositional Logic**
> - declarative sentence(t or f)
> - consists of objects, functions, logical connectives
> - always true : tautology
> - always false : contradiction
> - ∧ND | O∨* | IM→ | B⇔ |
>
> | p | q | p→q |
> |---|---|-----|
> | F | F |  T  |
> | F | T |  T  |
> | T | F |  F  |
> | T | T |  T  |
> 
> - P → Q
>     - Converse: Q → P
>     - Inverse: ~P → ~Q
>     - Contrapositive: ~Q → ~P
>     
> **First Order Logic**
>
Universal Quantifier: ∀ (for all)
Existential Quantifier: ∃ (for some)
>
> - Substitution: F[a/x]
> - Equality: Brother(John) = Smith

> 1. Universal Generalization
>   - eg. P(c): a byte contains 8 bits
>   - ∀x P(x): all bytes contain 8 bits
```math
$$ P(c) \over ∀x P(x) $$ 
```

> 2. Universal Instantiation (Elimination)
>   - eg. ∀x P(x): everyone likes ice cream
>   - P(c): john likes ice cream
```math
$$ ∀x P(x) \over P(c) $$ 
```

> 3. Existential Instantiation (Elimination)
>   - Can be applied only ONCE to replace existential sentence 
>   
```math
$$ ∃x P(x) \over P(c) $$ 
```

> 4. Existential Generalization
>   - eg. Pinky got good marks in maths
>   - therefore, someone got good marks.
```math
$$ P(c) \over ∃x P(x) $$ 
```

> - UNIFICATION
>     - to make expressions look identical, depends on substitution

> **FOL to CNF (Conjunctive Normal Form)**
> 
> Resolution
> 
> Semantic Networks

> Frames Representation
> 
