# Principles of AI

> A* algo
> Game playing MinMax
> Constraint Satisfaction

> <ins>**Propositional Logic**</ins>
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
> <ins>**First Order Logic**</ins>
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
>

> <ins>**FOL to CNF (Conjunctive Normal Form)**</ins>
> - Why? convenient when Quantifiers infront
> - these formulas are *prenex normal form*
> - Steps to Convert to CNF
>> 1. Eliminate → and ⇔
>> 2. Move all ¬ inward
>> 3. Standardize the variables apart (when necessary)
>> 4. Move all quantifiers to the front
> Resolution
> 
>
> Semantic Networks

> Frames Representation
> 
