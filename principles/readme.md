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
> - Steps to Convert to CNF:
>> 1. Eliminate → and ⇔
>> 2. Move all ¬ inward
>> 3. Standardize the variables apart (when necessary)
>> 4. Move all quantifiers to the front
>
> Resolution
> - Theorem proving technique by contradictions
> - Used to prove a conclusion
> - Steps for Resolution:
>> 1. Conversion of facts to FOL
>> 2. FOL to CNF
>> 3. Negate statements which needs to be proved
>> 4. Draw resolution graph
>> check goal with negated goal state
>> if negated goal + resolution goal = null, then it is true

> Semantic Networks (Propositional Net)
> - knowledge representation technique used for propositional logic
> - labelled directed graph
> - allows us to perform inheritance reasoning as members of a class will inherit all properties of a superclass.
| advantages | disadvantages |
|------------|---------------|
| convey meaning in transparent manner | links can only have binary relations |
| simple and easy to understand | no standard definition of link names | 


> Frames Representation
> - record like structure consisting of collection of attributes to describe an entity
| slot | slot values |
|------|-------------|
> - slot filter knowledge
> - used in applications including Natural language processing and machine visions
| advantages | disadvantages |
|------------|---------------|
| flexible | inference mechanism not smoothly proceeded |
| easy to add slots for new attributes and relations | generalized approach |
| easy to include default data |  |
| easy to understand |   |
