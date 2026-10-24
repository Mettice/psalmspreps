# Physics Form 4, Form Four Physics: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f4-physics`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1

Rules the computed answers use are listed in the subject’s library tests; every authored answer is in Part 2.

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `p4-1-which` | 1 | multiple choice, 1 | temperature |
| 2 | `p4-2-how` | 2 | multiple choice, 1 | temperature |
| 3 | `p4-3-define` | 3 | multiple choice, 1 | calorimetry |
| 4 | `p4-4-error` | 4 | multiple choice, 3 | calorimetry |
| 5 | `p4-4-error-card` (card c4p4-3) | 4 | multiple choice, 1 | calorimetry |
| 6 | `p4-5-flat` | 5 | multiple choice, 1 | latent-heat |
| 7 | `p4-5-evap` | 5 | multiple choice, 3 | latent-heat |
| 8 | `p4-5-evap-card` (card c4p5-3) | 5 | multiple choice, 1 | latent-heat |
| 9 | `p4-6-which` | 6 | multiple choice, 1 | heat-transfer |
| 10 | `p4-6-convect` | 6 | multiple choice, 1 | heat-transfer |
| 11 | `p4-6-radiate` | 6 | multiple choice, 2 | heat-transfer |
| 12 | `p4-6-radiate-card` (card c4p6-3) | 6 | multiple choice, 1 | heat-transfer |
| 13 | `p4-7-why` | 7 | multiple choice, 1 | expansion |
| 14 | `p4-7-bimetal` | 7 | multiple choice, 1 | expansion |
| 15 | `p4-7-water` | 7 | multiple choice, 2 | expansion |
| 16 | `p4-8-kind` | 8 | multiple choice, 1 | waves |
| 17 | `p4-8-medium` | 8 | multiple choice, 1 | waves |
| 18 | `p4-8-match` | 8 | matching, 2 | waves |
| 19 | `p4-8-energy` | 8 | multiple choice, 3 | waves |
| 20 | `p4-11-which` | 11 | multiple choice, 1 | wave-phenomena |
| 21 | `p4-11-diffract` | 11 | multiple choice, 2 | wave-phenomena |
| 22 | `p4-11-interfere` | 11 | multiple choice, 2 | wave-phenomena |
| 23 | `p4-11-match` | 11 | matching, 3 | wave-phenomena |
| 24 | `p4-11-diffract-card` (card c4p11-3) | 11 | multiple choice, 1 | wave-phenomena |
| 25 | `p4-12-compare` | 12 | multiple choice, 3 | waves |
| 26 | `p4-13-which` | 13 | multiple choice, 1 | sound |
| 27 | `p4-13-quality` | 13 | multiple choice, 2 | sound |
| 28 | `p4-13-medium` | 13 | multiple choice, 3 | sound |
| 29 | `p4-13-quality-card` (card c4p13-3) | 13 | multiple choice, 1 | sound |

### `p4-1-which` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which statement about heat and temperature is correct? | Heat is energy that flows; temperature tells how hot something is | Heat and temperature mean the same thing · A bigger object always has a higher temperature · Temperature is measured in joules | They are different: heat is energy in transit (joules); temperature is the degree of hotness (°C or K). · Size does not fix temperature: a cup and a bucket of water from the same tap are equally hot. · Temperature is measured in degrees Celsius or kelvin; heat is measured in joules. | Heat is energy that flows from a hotter body to a cooler one; temperature decides which way it flows. |
| A cup of tea and a bucket of water are both at 40 °C. Which holds more heat energy? | The bucket, because it has more particles | The cup, because it feels hotter · They hold the same, because the temperature is the same · Neither holds heat energy | They are at the same temperature, so neither feels hotter; the bucket simply holds more energy. · Equal temperature does not mean equal energy: the bucket has far more particles, each with energy. · Any body above absolute zero has internal energy. | At the same temperature each particle has the same average energy, so more particles means more energy in all. |
| Two objects touch. Which way does heat flow? | From the hotter one to the cooler one | From the bigger one to the smaller one · From the cooler one to the hotter one · Heat does not flow between touching objects | Size does not decide the direction; the temperature difference does. · Heat always flows the other way, from hot to cold, until the temperatures are equal. · Touching bodies at different temperatures always exchange heat. | Heat flows from high to low temperature until both reach the same temperature (thermal equilibrium). |
| What does 'thermal equilibrium' mean? | Two bodies in contact have reached the same temperature | Both bodies hold the same amount of heat energy · One body has no heat energy left · The bodies have the same mass | Equal temperature, not equal energy: a large body at the same temperature still holds more energy. · A body at any temperature above absolute zero still has internal energy. · Mass has nothing to do with it. | At thermal equilibrium there is no temperature difference, so no net flow of heat. |
| Which temperature scale starts at absolute zero? | The kelvin scale | The Celsius scale · The Fahrenheit scale · Every scale starts at absolute zero | Celsius starts at the melting point of ice, which is 273 K. · Fahrenheit has its own fixed points; it does not start at absolute zero. · Only the kelvin scale has its zero at absolute zero. | 0 K is absolute zero, the lowest possible temperature; T(K) = θ(°C) + 273. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A cup of tea and a bucket of water are both at 40 °C. Which holds more heat energy?

- ◻️ Neither holds heat energy  
  _↳ feedback if chosen: Any body above absolute zero has internal energy._
- ◻️ The cup, because it feels hotter  
  _↳ feedback if chosen: They are at the same temperature, so neither feels hotter; the bucket simply holds more energy._
- ✅ The bucket, because it has more particles
- ◻️ They hold the same, because the temperature is the same  
  _↳ feedback if chosen: Equal temperature does not mean equal energy: the bucket has far more particles, each with energy._

Full working after a second miss:

> At the same temperature each particle has the same average energy, so more particles means more energy in all.  
> So the answer is The bucket, because it has more particles.  

> What does 'thermal equilibrium' mean?

- ◻️ The bodies have the same mass  
  _↳ feedback if chosen: Mass has nothing to do with it._
- ✅ Two bodies in contact have reached the same temperature
- ◻️ One body has no heat energy left  
  _↳ feedback if chosen: A body at any temperature above absolute zero still has internal energy._
- ◻️ Both bodies hold the same amount of heat energy  
  _↳ feedback if chosen: Equal temperature, not equal energy: a large body at the same temperature still holds more energy._

Full working after a second miss:

> At thermal equilibrium there is no temperature difference, so no net flow of heat.  
> So the answer is Two bodies in contact have reached the same temperature.  

> A cup of tea and a bucket of water are both at 40 °C. Which holds more heat energy?

- ◻️ The cup, because it feels hotter  
  _↳ feedback if chosen: They are at the same temperature, so neither feels hotter; the bucket simply holds more energy._
- ◻️ They hold the same, because the temperature is the same  
  _↳ feedback if chosen: Equal temperature does not mean equal energy: the bucket has far more particles, each with energy._
- ✅ The bucket, because it has more particles
- ◻️ Neither holds heat energy  
  _↳ feedback if chosen: Any body above absolute zero has internal energy._

Full working after a second miss:

> At the same temperature each particle has the same average energy, so more particles means more energy in all.  
> So the answer is The bucket, because it has more particles.  

Sources: temperature (Form 4 Physics syllabus, Term 1: concept of heat and temperature, measurement of temperature; thermometry, liquid-in-glass thermometer, calibration using fixed points, clinical and laboratory thermometers)

### `p4-2-how` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is mercury or coloured alcohol used in a liquid-in-glass thermometer? | It expands evenly when heated and is easy to see | It is the cheapest liquid available · It never changes temperature · It turns to a gas as the temperature rises | Cost is not the reason; the liquid must expand evenly and be easy to see. · The liquid takes the temperature of its surroundings; that is how the thermometer works. · The liquid must stay liquid over the whole range of the scale. | A thermometric liquid expands by a steady amount for each degree, so the scale is evenly spaced. |
| What are the two fixed points used to calibrate a Celsius thermometer? | Pure melting ice (0 °C) and steam above boiling water (100 °C) | Room temperature and body temperature · Ice from a freezer and warm tap water · Any two temperatures that are easy to find | These vary from place to place and day to day, so they cannot be fixed points. · Freezer ice can be below 0 °C, and tap water has no fixed temperature. · Fixed points must be temperatures that are always the same under stated conditions. | Pure melting ice and steam at normal atmospheric pressure always give the same two temperatures. |
| Why is steam, not boiling water, used for the upper fixed point? | The steam above the water is at the boiling point, while the water may be overheated | Steam is hotter than boiling water · Water would break the thermometer · Steam is easier to hold still | Steam at normal pressure is at the same temperature as the boiling water, not hotter. · Boiling water does not break a laboratory thermometer. · Holding still is not the reason; the reading must be reliable. | Water touching a hot container can rise above 100 °C, but the steam just above it stays at the boiling point. |
| What is the constriction in a clinical thermometer for? | It stops the mercury running back, so the reading can be taken after removal | It makes the thermometer more sensitive · It stops the mercury from escaping · It shows where normal body temperature is | Sensitivity comes from the narrow bore and thin bulb, not the constriction. · The tube is sealed; the mercury cannot escape. · Normal body temperature is shown by a mark on the scale, not by the constriction. | The thread breaks at the constriction as the thermometer cools, so the highest reading stays. |
| Why does a clinical thermometer have a short range of about 35 °C to 42 °C? | A short range lets the degrees be spread out, so small changes can be read | Body temperature never goes outside that range · A longer tube would be too expensive · Mercury boils above 42 °C | A patient can be outside that range; the thermometer is simply not made to read it. · Cost is not the reason; the reason is accuracy over the useful range. · Mercury boils at about 357 °C. | Over a short range each degree takes more length on the scale, so 0.1 °C can be read. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the constriction in a clinical thermometer for?

- ◻️ It stops the mercury from escaping  
  _↳ feedback if chosen: The tube is sealed; the mercury cannot escape._
- ◻️ It makes the thermometer more sensitive  
  _↳ feedback if chosen: Sensitivity comes from the narrow bore and thin bulb, not the constriction._
- ◻️ It shows where normal body temperature is  
  _↳ feedback if chosen: Normal body temperature is shown by a mark on the scale, not by the constriction._
- ✅ It stops the mercury running back, so the reading can be taken after removal

Full working after a second miss:

> The thread breaks at the constriction as the thermometer cools, so the highest reading stays.  
> So the answer is It stops the mercury running back, so the reading can be taken after removal.  

> Why does a clinical thermometer have a short range of about 35 °C to 42 °C?

- ◻️ Mercury boils above 42 °C  
  _↳ feedback if chosen: Mercury boils at about 357 °C._
- ◻️ Body temperature never goes outside that range  
  _↳ feedback if chosen: A patient can be outside that range; the thermometer is simply not made to read it._
- ✅ A short range lets the degrees be spread out, so small changes can be read
- ◻️ A longer tube would be too expensive  
  _↳ feedback if chosen: Cost is not the reason; the reason is accuracy over the useful range._

Full working after a second miss:

> Over a short range each degree takes more length on the scale, so 0.1 °C can be read.  
> So the answer is A short range lets the degrees be spread out, so small changes can be read.  

> What is the constriction in a clinical thermometer for?

- ✅ It stops the mercury running back, so the reading can be taken after removal
- ◻️ It shows where normal body temperature is  
  _↳ feedback if chosen: Normal body temperature is shown by a mark on the scale, not by the constriction._
- ◻️ It makes the thermometer more sensitive  
  _↳ feedback if chosen: Sensitivity comes from the narrow bore and thin bulb, not the constriction._
- ◻️ It stops the mercury from escaping  
  _↳ feedback if chosen: The tube is sealed; the mercury cannot escape._

Full working after a second miss:

> The thread breaks at the constriction as the thermometer cools, so the highest reading stays.  
> So the answer is It stops the mercury running back, so the reading can be taken after removal.  

Sources: temperature (Form 4 Physics syllabus, Term 1: concept of heat and temperature, measurement of temperature; thermometry, liquid-in-glass thermometer, calibration using fixed points, clinical and laboratory thermometers)

### `p4-3-define` · Lesson 3 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the specific heat capacity of a material? | The heat needed to raise the temperature of {1} kg of it by {1} K | The heat needed to raise the whole body by {1} K · The heat needed to melt {1} kg of it · The temperature it reaches when heated | That is heat capacity C, in J/K, which depends on how much of the material there is. · That is specific latent heat of fusion; melting happens at a constant temperature. · Specific heat capacity is an energy per kilogram per kelvin, not a temperature. | 'Specific' means per kilogram: c = Q ÷ (mΔθ), in J/(kg·K). |
| What is the heat capacity of a body? | The heat needed to raise the temperature of that whole body by {1} K | The heat needed to raise {1} kg of it by {1} K · The total heat energy stored in the body · The highest temperature the body can reach | That is specific heat capacity, which is per kilogram and depends only on the material. · Heat capacity is about the heat needed for a rise of {1} K, not the energy already stored. · A body has no highest temperature of this kind; heat capacity is an energy per kelvin. | C = Q ÷ Δθ, in J/K. A bigger body of the same material has a bigger heat capacity. |
| What is the unit of specific heat capacity? | J/(kg·K) | J/K · J/kg · J | J/K is the unit of heat capacity, which is for a whole body. · J/kg is the unit of specific latent heat, where there is no temperature change. · The joule is the unit of heat itself, not of a capacity. | c = Q ÷ (mΔθ): joules divided by kilograms and by kelvin. |
| Water has a specific heat capacity of {4200} J/(kg·K) and copper {400} J/(kg·K). Which warms up faster for the same heat and mass? | The copper, because less heat is needed for each degree | The water, because it has the larger value · They warm at the same rate · Neither warms up | A large c means more heat is needed for each degree, so water warms more slowly. · The two values differ by more than ten times, so the rates differ greatly. · Both warm; the question is which warms faster. | Δθ = Q ÷ (mc): the smaller the c, the bigger the temperature rise for the same heat. |
| Why is water used as the coolant in a car engine? | It has a high specific heat capacity, so it carries away a lot of heat for a small rise in temperature | It has a low specific heat capacity, so it heats up quickly · It conducts heat better than any metal · It never boils inside an engine | A low value would mean it heated quickly and carried away little heat. · Metals conduct far better than water; what matters here is the heat water can carry away. · Water can boil in an engine, which is why the system is kept under pressure. | With c = {4200} J/(kg·K), each kilogram takes in {4200} J for every degree it rises. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Water has a specific heat capacity of 4200 J/(kg·K) and copper 400 J/(kg·K). Which warms up faster for the same heat and mass?

- ◻️ They warm at the same rate  
  _↳ feedback if chosen: The two values differ by more than ten times, so the rates differ greatly._
- ◻️ The water, because it has the larger value  
  _↳ feedback if chosen: A large c means more heat is needed for each degree, so water warms more slowly._
- ✅ The copper, because less heat is needed for each degree
- ◻️ Neither warms up  
  _↳ feedback if chosen: Both warm; the question is which warms faster._

Full working after a second miss:

> Δθ = Q ÷ (mc): the smaller the c, the bigger the temperature rise for the same heat.  
> So the answer is The copper, because less heat is needed for each degree.  

> What is the heat capacity of a body?

- ◻️ The highest temperature the body can reach  
  _↳ feedback if chosen: A body has no highest temperature of this kind; heat capacity is an energy per kelvin._
- ◻️ The heat needed to raise 1 kg of it by 1 K  
  _↳ feedback if chosen: That is specific heat capacity, which is per kilogram and depends only on the material._
- ✅ The heat needed to raise the temperature of that whole body by 1 K
- ◻️ The total heat energy stored in the body  
  _↳ feedback if chosen: Heat capacity is about the heat needed for a rise of 1 K, not the energy already stored._

Full working after a second miss:

> C = Q ÷ Δθ, in J/K. A bigger body of the same material has a bigger heat capacity.  
> So the answer is The heat needed to raise the temperature of that whole body by 1 K.  

> What is the heat capacity of a body?

- ◻️ The highest temperature the body can reach  
  _↳ feedback if chosen: A body has no highest temperature of this kind; heat capacity is an energy per kelvin._
- ◻️ The total heat energy stored in the body  
  _↳ feedback if chosen: Heat capacity is about the heat needed for a rise of 1 K, not the energy already stored._
- ◻️ The heat needed to raise 1 kg of it by 1 K  
  _↳ feedback if chosen: That is specific heat capacity, which is per kilogram and depends only on the material._
- ✅ The heat needed to raise the temperature of that whole body by 1 K

Full working after a second miss:

> C = Q ÷ Δθ, in J/K. A bigger body of the same material has a bigger heat capacity.  
> So the answer is The heat needed to raise the temperature of that whole body by 1 K.  

Sources: calorimetry (Form 4 Physics syllabus, Term 1: heat capacity and specific heat capacity, measurement of c for a solid and for a liquid, calculations using Q = mcΔθ)

### `p4-4-error` · Lesson 4 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| The calorimeter is not lagged, so heat escapes to the room. How does this affect the value found for c? | It comes out too large, because some of the energy counted did not reach the liquid | It comes out too small, because the liquid gets less energy · It is not affected, because the energy supplied is measured exactly · It comes out too large, because the temperature rise is bigger | The energy VIt is counted in full, so the calculated c is too large, not too small. · The energy is measured exactly, but not all of it reaches the liquid. · Losing heat makes the temperature rise smaller, not bigger. | All of VIt is counted but Δθ comes out small, and c = VIt ÷ (mΔθ). |
| Why is the liquid stirred during the electrical method? | So that the whole liquid is at one temperature when the thermometer is read | To make the liquid heat up faster · To stop the liquid from boiling · To spread the electrical current through the liquid | Stirring moves heat about but does not add energy, so it does not speed up the heating. · The liquid is not heated to its boiling point in this experiment. · The current stays in the heater; it does not pass through the liquid. | Without stirring, the liquid near the heater is hotter than the rest and the reading is too high. |
| Why is the experiment often started a few degrees below room temperature? | Heat gained from the room at the start then roughly cancels the heat lost to it at the end | Cold liquid has a larger specific heat capacity · The heater works better in a cold liquid · It makes the temperature rise larger | Specific heat capacity hardly changes over such a small range of temperature. · The heater supplies the same power whatever the temperature of the liquid. · The rise measured is the same; what changes is how the losses cancel. | Below room temperature heat flows in; above it heat flows out. Starting below makes the two roughly cancel. |
| Why should the heating time be kept fairly short? | The longer the liquid stays hot, the more heat escapes to the room | A long time would use too much electricity · A long time would melt the calorimeter · The heater can only run for a short time | The cost of the electricity is not a source of error in the measurement. · The temperatures reached are far below the melting point of the calorimeter. · An immersion heater can run for much longer than the experiment needs. | Heat loss grows with the time spent above room temperature, so a short run keeps the error small. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is the experiment often started a few degrees below room temperature?

- ◻️ Cold liquid has a larger specific heat capacity  
  _↳ feedback if chosen: Specific heat capacity hardly changes over such a small range of temperature._
- ✅ Heat gained from the room at the start then roughly cancels the heat lost to it at the end
- ◻️ It makes the temperature rise larger  
  _↳ feedback if chosen: The rise measured is the same; what changes is how the losses cancel._
- ◻️ The heater works better in a cold liquid  
  _↳ feedback if chosen: The heater supplies the same power whatever the temperature of the liquid._

Full working after a second miss:

> Below room temperature heat flows in; above it heat flows out. Starting below makes the two roughly cancel.  
> So the answer is Heat gained from the room at the start then roughly cancels the heat lost to it at the end.  

> The calorimeter is not lagged, so heat escapes to the room. How does this affect the value found for c?

- ◻️ It comes out too large, because the temperature rise is bigger  
  _↳ feedback if chosen: Losing heat makes the temperature rise smaller, not bigger._
- ◻️ It comes out too small, because the liquid gets less energy  
  _↳ feedback if chosen: The energy VIt is counted in full, so the calculated c is too large, not too small._
- ◻️ It is not affected, because the energy supplied is measured exactly  
  _↳ feedback if chosen: The energy is measured exactly, but not all of it reaches the liquid._
- ✅ It comes out too large, because some of the energy counted did not reach the liquid

Full working after a second miss:

> All of VIt is counted but Δθ comes out small, and c = VIt ÷ (mΔθ).  
> So the answer is It comes out too large, because some of the energy counted did not reach the liquid.  

> Why is the experiment often started a few degrees below room temperature?

- ◻️ Cold liquid has a larger specific heat capacity  
  _↳ feedback if chosen: Specific heat capacity hardly changes over such a small range of temperature._
- ◻️ It makes the temperature rise larger  
  _↳ feedback if chosen: The rise measured is the same; what changes is how the losses cancel._
- ✅ Heat gained from the room at the start then roughly cancels the heat lost to it at the end
- ◻️ The heater works better in a cold liquid  
  _↳ feedback if chosen: The heater supplies the same power whatever the temperature of the liquid._

Full working after a second miss:

> Below room temperature heat flows in; above it heat flows out. Starting below makes the two roughly cancel.  
> So the answer is Heat gained from the room at the start then roughly cancels the heat lost to it at the end.  

Sources: calorimetry (Form 4 Physics syllabus, Term 1: heat capacity and specific heat capacity, measurement of c for a solid and for a liquid, calculations using Q = mcΔθ)

### `p4-4-error-card` · Lesson 4 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| The calorimeter is not lagged, so heat escapes to the room. How does this affect the value found for c? | It comes out too large, because some of the energy counted did not reach the liquid | It comes out too small, because the liquid gets less energy · It is not affected, because the energy supplied is measured exactly · It comes out too large, because the temperature rise is bigger | The energy VIt is counted in full, so the calculated c is too large, not too small. · The energy is measured exactly, but not all of it reaches the liquid. · Losing heat makes the temperature rise smaller, not bigger. | All of VIt is counted but Δθ comes out small, and c = VIt ÷ (mΔθ). |
| Why is the liquid stirred during the electrical method? | So that the whole liquid is at one temperature when the thermometer is read | To make the liquid heat up faster · To stop the liquid from boiling · To spread the electrical current through the liquid | Stirring moves heat about but does not add energy, so it does not speed up the heating. · The liquid is not heated to its boiling point in this experiment. · The current stays in the heater; it does not pass through the liquid. | Without stirring, the liquid near the heater is hotter than the rest and the reading is too high. |
| Why is the experiment often started a few degrees below room temperature? | Heat gained from the room at the start then roughly cancels the heat lost to it at the end | Cold liquid has a larger specific heat capacity · The heater works better in a cold liquid · It makes the temperature rise larger | Specific heat capacity hardly changes over such a small range of temperature. · The heater supplies the same power whatever the temperature of the liquid. · The rise measured is the same; what changes is how the losses cancel. | Below room temperature heat flows in; above it heat flows out. Starting below makes the two roughly cancel. |
| Why should the heating time be kept fairly short? | The longer the liquid stays hot, the more heat escapes to the room | A long time would use too much electricity · A long time would melt the calorimeter · The heater can only run for a short time | The cost of the electricity is not a source of error in the measurement. · The temperatures reached are far below the melting point of the calorimeter. · An immersion heater can run for much longer than the experiment needs. | Heat loss grows with the time spent above room temperature, so a short run keeps the error small. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> The calorimeter is not lagged, so heat escapes to the room. How does this affect the value found for c?

- ◻️ It comes out too large, because the temperature rise is bigger  
  _↳ feedback if chosen: Losing heat makes the temperature rise smaller, not bigger._
- ✅ It comes out too large, because some of the energy counted did not reach the liquid
- ◻️ It comes out too small, because the liquid gets less energy  
  _↳ feedback if chosen: The energy VIt is counted in full, so the calculated c is too large, not too small._
- ◻️ It is not affected, because the energy supplied is measured exactly  
  _↳ feedback if chosen: The energy is measured exactly, but not all of it reaches the liquid._

Full working after a second miss:

> All of VIt is counted but Δθ comes out small, and c = VIt ÷ (mΔθ).  
> So the answer is It comes out too large, because some of the energy counted did not reach the liquid.  

> The calorimeter is not lagged, so heat escapes to the room. How does this affect the value found for c?

- ◻️ It is not affected, because the energy supplied is measured exactly  
  _↳ feedback if chosen: The energy is measured exactly, but not all of it reaches the liquid._
- ✅ It comes out too large, because some of the energy counted did not reach the liquid
- ◻️ It comes out too small, because the liquid gets less energy  
  _↳ feedback if chosen: The energy VIt is counted in full, so the calculated c is too large, not too small._
- ◻️ It comes out too large, because the temperature rise is bigger  
  _↳ feedback if chosen: Losing heat makes the temperature rise smaller, not bigger._

Full working after a second miss:

> All of VIt is counted but Δθ comes out small, and c = VIt ÷ (mΔθ).  
> So the answer is It comes out too large, because some of the energy counted did not reach the liquid.  

> Why is the liquid stirred during the electrical method?

- ◻️ To make the liquid heat up faster  
  _↳ feedback if chosen: Stirring moves heat about but does not add energy, so it does not speed up the heating._
- ◻️ To spread the electrical current through the liquid  
  _↳ feedback if chosen: The current stays in the heater; it does not pass through the liquid._
- ✅ So that the whole liquid is at one temperature when the thermometer is read
- ◻️ To stop the liquid from boiling  
  _↳ feedback if chosen: The liquid is not heated to its boiling point in this experiment._

Full working after a second miss:

> Without stirring, the liquid near the heater is hotter than the rest and the reading is too high.  
> So the answer is So that the whole liquid is at one temperature when the thermometer is read.  

Sources: calorimetry (Form 4 Physics syllabus, Term 1: heat capacity and specific heat capacity, measurement of c for a solid and for a liquid, calculations using Q = mcΔθ)

### `p4-5-flat` · Lesson 5 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Ice at {0} °C is heated steadily until it has all melted. What happens to the temperature while it melts? | It stays at {0} °C | It rises steadily · It falls, because melting is cooling · It rises, then falls | The temperature rises again only once all the ice has melted. · Heat is being taken in, so the temperature does not fall. · It stays constant until the melting is complete. | During a change of state the heat separates the particles instead of speeding them up. |
| Where does the energy go while ice is melting at {0} °C? | It separates the particles from their fixed positions | It makes the particles move faster · It is destroyed · It is stored as temperature | Faster particles would mean a higher temperature, but the temperature stays the same. · Energy is never destroyed; it changes form or place. · Temperature is not a store of energy; it is the degree of hotness. | Latent heat does the work of breaking the forces holding the particles in place. |
| Why does steam at {100} °C scald more badly than water at {100} °C? | The steam gives out its latent heat of vaporisation as it condenses on the skin | Steam is hotter than boiling water · Steam travels faster than water · Water cools before it touches the skin | Both are at {100} °C; the difference is the latent heat, not the temperature. · Speed is not the reason; the extra energy released is. · The water is still at {100} °C when it lands. | Each kilogram of steam gives out {2260000} J as it condenses, on top of the heat released as it then cools. |
| What is the specific latent heat of fusion of a substance? | The heat needed to change {1} kg of it from solid to liquid at its melting point | The heat needed to raise {1} kg of it by {1} K · The heat needed to boil {1} kg of it · The temperature at which it melts | That is specific heat capacity, where the temperature does change. · That is the specific latent heat of vaporisation. · Latent heat is an energy per kilogram, not a temperature. | Fusion means melting: Q = ml_f, with l_f in J/kg and no change of temperature. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the specific latent heat of fusion of a substance?

- ◻️ The temperature at which it melts  
  _↳ feedback if chosen: Latent heat is an energy per kilogram, not a temperature._
- ◻️ The heat needed to boil 1 kg of it  
  _↳ feedback if chosen: That is the specific latent heat of vaporisation._
- ◻️ The heat needed to raise 1 kg of it by 1 K  
  _↳ feedback if chosen: That is specific heat capacity, where the temperature does change._
- ✅ The heat needed to change 1 kg of it from solid to liquid at its melting point

Full working after a second miss:

> Fusion means melting: Q = ml_f, with l_f in J/kg and no change of temperature.  
> So the answer is The heat needed to change 1 kg of it from solid to liquid at its melting point.  

> Why does steam at 100 °C scald more badly than water at 100 °C?

- ◻️ Steam travels faster than water  
  _↳ feedback if chosen: Speed is not the reason; the extra energy released is._
- ✅ The steam gives out its latent heat of vaporisation as it condenses on the skin
- ◻️ Steam is hotter than boiling water  
  _↳ feedback if chosen: Both are at 100 °C; the difference is the latent heat, not the temperature._
- ◻️ Water cools before it touches the skin  
  _↳ feedback if chosen: The water is still at 100 °C when it lands._

Full working after a second miss:

> Each kilogram of steam gives out 2 260 000 J as it condenses, on top of the heat released as it then cools.  
> So the answer is The steam gives out its latent heat of vaporisation as it condenses on the skin.  

> Where does the energy go while ice is melting at 0 °C?

- ◻️ It makes the particles move faster  
  _↳ feedback if chosen: Faster particles would mean a higher temperature, but the temperature stays the same._
- ✅ It separates the particles from their fixed positions
- ◻️ It is stored as temperature  
  _↳ feedback if chosen: Temperature is not a store of energy; it is the degree of hotness._
- ◻️ It is destroyed  
  _↳ feedback if chosen: Energy is never destroyed; it changes form or place._

Full working after a second miss:

> Latent heat does the work of breaking the forces holding the particles in place.  
> So the answer is It separates the particles from their fixed positions.  

Sources: latent-heat (Form 4 Physics syllabus, Term 1: latent heat and specific latent heat, calculations using Q = ml, cooling effect of evaporation)

### `p4-5-evap` · Lesson 5 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does a clay pot keep drinking water cool on a hot day? | Water seeps through the clay and evaporates, taking latent heat from the water left inside | The clay stops heat from the sun reaching the water · Clay is naturally cold · The water inside freezes a little | A glazed pot of the same clay does not keep the water nearly as cool: the evaporation does the work. · A material is not cold by itself; it takes the temperature of its surroundings. · The water stays well above {0} °C; it is cooled, not frozen. | Evaporation from the outside takes latent heat of vaporisation from the pot and the water in it. |
| Why does sweating cool the body? | The sweat evaporates and takes latent heat from the skin | Sweat is colder than the body · Sweat carries heat away as a liquid running off · Sweating uses up energy in the muscles | Sweat leaves the body at body temperature; it is not cold. · Sweat that runs off without evaporating cools very little; that is why a humid day feels worse. · The cooling happens at the skin surface, not in the muscles. | The fastest particles escape from the sweat, so the skin loses energy and cools. |
| On which day will washing on a line dry fastest? | A hot, dry and windy day | A hot, still and humid day · A cool, still and humid day · A cool, windy and humid day | Still, humid air above the cloth slows evaporation even when it is hot. · Cool, still and humid is the slowest of all. · Wind helps, but humid air can take up little more water. | Evaporation is faster when it is hotter, when the air is drier, and when wind carries the vapour away. |
| Why does methylated spirit on the back of the hand feel colder than water does? | It evaporates faster, so it takes latent heat from the skin more quickly | It is stored at a lower temperature · It conducts heat better than water · It is a better insulator than water | Both liquids are at room temperature before they are used. · Conduction is not the main effect here; the rate of evaporation is. · An insulator would slow the loss of heat, not speed it up. | A liquid that evaporates quickly takes its latent heat from the skin quickly, so the skin cools fast. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does methylated spirit on the back of the hand feel colder than water does?

- ◻️ It is a better insulator than water  
  _↳ feedback if chosen: An insulator would slow the loss of heat, not speed it up._
- ◻️ It conducts heat better than water  
  _↳ feedback if chosen: Conduction is not the main effect here; the rate of evaporation is._
- ✅ It evaporates faster, so it takes latent heat from the skin more quickly
- ◻️ It is stored at a lower temperature  
  _↳ feedback if chosen: Both liquids are at room temperature before they are used._

Full working after a second miss:

> A liquid that evaporates quickly takes its latent heat from the skin quickly, so the skin cools fast.  
> So the answer is It evaporates faster, so it takes latent heat from the skin more quickly.  

> On which day will washing on a line dry fastest?

- ✅ A hot, dry and windy day
- ◻️ A cool, still and humid day  
  _↳ feedback if chosen: Cool, still and humid is the slowest of all._
- ◻️ A hot, still and humid day  
  _↳ feedback if chosen: Still, humid air above the cloth slows evaporation even when it is hot._
- ◻️ A cool, windy and humid day  
  _↳ feedback if chosen: Wind helps, but humid air can take up little more water._

Full working after a second miss:

> Evaporation is faster when it is hotter, when the air is drier, and when wind carries the vapour away.  
> So the answer is A hot, dry and windy day.  

> Why does sweating cool the body?

- ◻️ Sweat is colder than the body  
  _↳ feedback if chosen: Sweat leaves the body at body temperature; it is not cold._
- ◻️ Sweating uses up energy in the muscles  
  _↳ feedback if chosen: The cooling happens at the skin surface, not in the muscles._
- ✅ The sweat evaporates and takes latent heat from the skin
- ◻️ Sweat carries heat away as a liquid running off  
  _↳ feedback if chosen: Sweat that runs off without evaporating cools very little; that is why a humid day feels worse._

Full working after a second miss:

> The fastest particles escape from the sweat, so the skin loses energy and cools.  
> So the answer is The sweat evaporates and takes latent heat from the skin.  

Sources: latent-heat (Form 4 Physics syllabus, Term 1: latent heat and specific latent heat, calculations using Q = ml, cooling effect of evaporation)

### `p4-5-evap-card` · Lesson 5 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does a clay pot keep drinking water cool on a hot day? | Water seeps through the clay and evaporates, taking latent heat from the water left inside | The clay stops heat from the sun reaching the water · Clay is naturally cold · The water inside freezes a little | A glazed pot of the same clay does not keep the water nearly as cool: the evaporation does the work. · A material is not cold by itself; it takes the temperature of its surroundings. · The water stays well above {0} °C; it is cooled, not frozen. | Evaporation from the outside takes latent heat of vaporisation from the pot and the water in it. |
| Why does sweating cool the body? | The sweat evaporates and takes latent heat from the skin | Sweat is colder than the body · Sweat carries heat away as a liquid running off · Sweating uses up energy in the muscles | Sweat leaves the body at body temperature; it is not cold. · Sweat that runs off without evaporating cools very little; that is why a humid day feels worse. · The cooling happens at the skin surface, not in the muscles. | The fastest particles escape from the sweat, so the skin loses energy and cools. |
| On which day will washing on a line dry fastest? | A hot, dry and windy day | A hot, still and humid day · A cool, still and humid day · A cool, windy and humid day | Still, humid air above the cloth slows evaporation even when it is hot. · Cool, still and humid is the slowest of all. · Wind helps, but humid air can take up little more water. | Evaporation is faster when it is hotter, when the air is drier, and when wind carries the vapour away. |
| Why does methylated spirit on the back of the hand feel colder than water does? | It evaporates faster, so it takes latent heat from the skin more quickly | It is stored at a lower temperature · It conducts heat better than water · It is a better insulator than water | Both liquids are at room temperature before they are used. · Conduction is not the main effect here; the rate of evaporation is. · An insulator would slow the loss of heat, not speed it up. | A liquid that evaporates quickly takes its latent heat from the skin quickly, so the skin cools fast. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does a clay pot keep drinking water cool on a hot day?

- ◻️ The water inside freezes a little  
  _↳ feedback if chosen: The water stays well above 0 °C; it is cooled, not frozen._
- ✅ Water seeps through the clay and evaporates, taking latent heat from the water left inside
- ◻️ The clay stops heat from the sun reaching the water  
  _↳ feedback if chosen: A glazed pot of the same clay does not keep the water nearly as cool: the evaporation does the work._
- ◻️ Clay is naturally cold  
  _↳ feedback if chosen: A material is not cold by itself; it takes the temperature of its surroundings._

Full working after a second miss:

> Evaporation from the outside takes latent heat of vaporisation from the pot and the water in it.  
> So the answer is Water seeps through the clay and evaporates, taking latent heat from the water left inside.  

> On which day will washing on a line dry fastest?

- ✅ A hot, dry and windy day
- ◻️ A cool, windy and humid day  
  _↳ feedback if chosen: Wind helps, but humid air can take up little more water._
- ◻️ A hot, still and humid day  
  _↳ feedback if chosen: Still, humid air above the cloth slows evaporation even when it is hot._
- ◻️ A cool, still and humid day  
  _↳ feedback if chosen: Cool, still and humid is the slowest of all._

Full working after a second miss:

> Evaporation is faster when it is hotter, when the air is drier, and when wind carries the vapour away.  
> So the answer is A hot, dry and windy day.  

> On which day will washing on a line dry fastest?

- ◻️ A cool, windy and humid day  
  _↳ feedback if chosen: Wind helps, but humid air can take up little more water._
- ◻️ A hot, still and humid day  
  _↳ feedback if chosen: Still, humid air above the cloth slows evaporation even when it is hot._
- ◻️ A cool, still and humid day  
  _↳ feedback if chosen: Cool, still and humid is the slowest of all._
- ✅ A hot, dry and windy day

Full working after a second miss:

> Evaporation is faster when it is hotter, when the air is drier, and when wind carries the vapour away.  
> So the answer is A hot, dry and windy day.  

Sources: latent-heat (Form 4 Physics syllabus, Term 1: latent heat and specific latent heat, calculations using Q = ml, cooling effect of evaporation)

### `p4-6-which` · Lesson 6 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A metal spoon left in hot soup becomes hot at the handle. Which method of heat transfer is this? | Conduction | Convection · Radiation · Evaporation | Convection needs a fluid to move; the spoon is solid and stays still. · Radiation needs no contact, but here the heat travels through the metal itself. · Evaporation is a change of state at a liquid surface, not a way of carrying heat along a spoon. | In a solid, heat passes from particle to particle and, in a metal, by free electrons: that is conduction. |
| Why is the heating element of a water heater placed near the bottom of the tank? | So that the warm water rises and sets up a convection current | So that the heat can radiate upwards · Because heat cannot travel downwards at all · To keep the element away from the steam | Radiation travels in all directions and is not the main effect in water. · Heat can travel downwards by conduction and radiation; the point is that warm water rises. · Keeping it away from steam is not the reason for heating from below. | Warm water expands, becomes less dense and rises, while cooler water sinks to take its place: a convection current heats the whole tank. |
| Which surface is the best absorber and emitter of radiation? | A dull black surface | A shiny silver surface · A white painted surface · All surfaces are equally good | A shiny silver surface reflects radiation and is a poor absorber and emitter. · White reflects much of the radiation that falls on it. · Colour and texture change how well a surface absorbs and emits. | Dull black surfaces absorb and emit radiation best; shiny, light surfaces reflect it. |
| How does heat from the Sun reach the Earth? | By radiation, which needs no material medium | By conduction through the air · By convection currents in space · By all three methods equally | There is almost no matter between the Sun and the atmosphere to conduct through. · Convection needs a fluid to move; space is very nearly empty. · Only one of the three can cross a vacuum, so they are not equal here. | Radiation is electromagnetic waves, so it can cross a vacuum. Conduction and convection cannot. |
| Why is a vacuum flask silvered on both sides of the double wall? | To reflect radiation back, so little heat enters or leaves | To stop conduction through the glass · To make the flask look attractive · To stop convection inside the liquid | Conduction is stopped by the vacuum between the walls, not by the silvering. · The appearance is not the reason; the silvering is inside the double wall. · Convection inside the liquid is not what the silvering prevents. | Shiny silver surfaces are poor emitters and good reflectors, so radiation is turned back. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which surface is the best absorber and emitter of radiation?

- ◻️ All surfaces are equally good  
  _↳ feedback if chosen: Colour and texture change how well a surface absorbs and emits._
- ◻️ A white painted surface  
  _↳ feedback if chosen: White reflects much of the radiation that falls on it._
- ◻️ A shiny silver surface  
  _↳ feedback if chosen: A shiny silver surface reflects radiation and is a poor absorber and emitter._
- ✅ A dull black surface

Full working after a second miss:

> Dull black surfaces absorb and emit radiation best; shiny, light surfaces reflect it.  
> So the answer is A dull black surface.  

> Why is the heating element of a water heater placed near the bottom of the tank?

- ✅ So that the warm water rises and sets up a convection current
- ◻️ To keep the element away from the steam  
  _↳ feedback if chosen: Keeping it away from steam is not the reason for heating from below._
- ◻️ So that the heat can radiate upwards  
  _↳ feedback if chosen: Radiation travels in all directions and is not the main effect in water._
- ◻️ Because heat cannot travel downwards at all  
  _↳ feedback if chosen: Heat can travel downwards by conduction and radiation; the point is that warm water rises._

Full working after a second miss:

> Warm water expands, becomes less dense and rises, while cooler water sinks to take its place: a convection current heats the whole tank.  
> So the answer is So that the warm water rises and sets up a convection current.  

> How does heat from the Sun reach the Earth?

- ◻️ By all three methods equally  
  _↳ feedback if chosen: Only one of the three can cross a vacuum, so they are not equal here._
- ✅ By radiation, which needs no material medium
- ◻️ By conduction through the air  
  _↳ feedback if chosen: There is almost no matter between the Sun and the atmosphere to conduct through._
- ◻️ By convection currents in space  
  _↳ feedback if chosen: Convection needs a fluid to move; space is very nearly empty._

Full working after a second miss:

> Radiation is electromagnetic waves, so it can cross a vacuum. Conduction and convection cannot.  
> So the answer is By radiation, which needs no material medium.  

Sources: heat-transfer (Form 4 Physics syllabus, Term 1: heat transfer by conduction, convection and radiation and their applications)

### `p4-6-convect` · Lesson 6 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does warm water rise in a convection current? | It expands, so the same mass fills a larger volume and its density falls | Warm water is heavier than cold water · Heat always travels upwards · The water is pushed up by the heater | Warming expands water, so it becomes LESS dense, not heavier. · Heat travels in all directions; here it is the moving fluid that carries it upwards. · The heater does not push the water; the difference in density does. | Density = mass ÷ volume, and less dense fluid floats above denser fluid. |
| In which materials can convection carry heat? | Only in liquids and gases, because the material itself must move | In solids, liquids and gases alike · Only in solids · Only in a vacuum | The particles of a solid are held in place, so they cannot carry heat across the body. · Convection needs a fluid that can flow, which a solid cannot do. · A vacuum has no particles at all; only radiation crosses it. | Convection moves heat by moving the fluid itself, so it needs a liquid or a gas. |
| Why is the cooling unit of a refrigerator placed at the top? | Air cooled at the top becomes denser and sinks, cooling the whole cabinet | Cold air rises, so it must start at the top · The food at the top needs the most cooling · There is no room for it at the bottom | Cold air is denser than warm air, so it sinks. · All the food needs cooling; the placing is about the circulation. · The placing is chosen for the convection current, not for space. | Cooled air sinks and warmer air rises to be cooled, so a current circulates through the fridge. |
| Smoke is held over one chimney of a box with two chimneys and a candle under the other. What is seen, and why? | The smoke is drawn down one chimney and out of the other, showing a convection current | The smoke rises straight up from both chimneys · The smoke stays still above the box · The smoke is blown away from the box | Air leaves above the candle, so smoke cannot rise from that chimney. · The candle sets the air moving, so the smoke does move. · Nothing blows the smoke away; the current pulls it in. | Warm air above the candle rises and leaves, so cooler air (with the smoke) is drawn down the other chimney. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is the cooling unit of a refrigerator placed at the top?

- ✅ Air cooled at the top becomes denser and sinks, cooling the whole cabinet
- ◻️ Cold air rises, so it must start at the top  
  _↳ feedback if chosen: Cold air is denser than warm air, so it sinks._
- ◻️ The food at the top needs the most cooling  
  _↳ feedback if chosen: All the food needs cooling; the placing is about the circulation._
- ◻️ There is no room for it at the bottom  
  _↳ feedback if chosen: The placing is chosen for the convection current, not for space._

Full working after a second miss:

> Cooled air sinks and warmer air rises to be cooled, so a current circulates through the fridge.  
> So the answer is Air cooled at the top becomes denser and sinks, cooling the whole cabinet.  

> Why does warm water rise in a convection current?

- ◻️ Heat always travels upwards  
  _↳ feedback if chosen: Heat travels in all directions; here it is the moving fluid that carries it upwards._
- ◻️ The water is pushed up by the heater  
  _↳ feedback if chosen: The heater does not push the water; the difference in density does._
- ◻️ Warm water is heavier than cold water  
  _↳ feedback if chosen: Warming expands water, so it becomes LESS dense, not heavier._
- ✅ It expands, so the same mass fills a larger volume and its density falls

Full working after a second miss:

> Density = mass ÷ volume, and less dense fluid floats above denser fluid.  
> So the answer is It expands, so the same mass fills a larger volume and its density falls.  

> Why does warm water rise in a convection current?

- ◻️ Heat always travels upwards  
  _↳ feedback if chosen: Heat travels in all directions; here it is the moving fluid that carries it upwards._
- ◻️ Warm water is heavier than cold water  
  _↳ feedback if chosen: Warming expands water, so it becomes LESS dense, not heavier._
- ◻️ The water is pushed up by the heater  
  _↳ feedback if chosen: The heater does not push the water; the difference in density does._
- ✅ It expands, so the same mass fills a larger volume and its density falls

Full working after a second miss:

> Density = mass ÷ volume, and less dense fluid floats above denser fluid.  
> So the answer is It expands, so the same mass fills a larger volume and its density falls.  

Sources: heat-transfer (Form 4 Physics syllabus, Term 1: heat transfer by conduction, convection and radiation and their applications)

### `p4-6-radiate` · Lesson 6 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Two cans of hot water are alike except that one is dull black and the other shiny silver. Which cools faster? | The dull black one, because a dull black surface is a better emitter of radiation | The shiny one, because shiny metal conducts heat away · Both cool at the same rate · The dull black one, because black absorbs more heat | The cans are the same metal; the paint changes how well they emit, not how they conduct. · The surfaces differ, so they radiate at different rates. · These cans are hotter than the room, so they are emitting. The answer is right but the reason is not. | Both lose heat by conduction and convection alike; the dull black surface emits radiation best. |
| Which surface takes in radiation best? | A dull black surface | A shiny silver surface · A white painted surface · A polished glass surface | A shiny silver surface reflects most of the radiation that falls on it. · White reflects much of the radiation. · Polished glass reflects and lets radiation through rather than absorbing it. | A good absorber is also a good emitter: dull black is best at both. |
| Why can radiation reach the Earth from the Sun? | Radiation is electromagnetic waves, which need no material medium | The air between carries it by conduction · Convection currents cross space · Space is full of particles that pass it along | There is almost no matter between the Sun and the atmosphere to conduct through. · Convection needs a fluid to flow; space is very nearly empty. · Space is nearly empty, so there is nothing to pass heat along. | Only radiation can cross a vacuum; conduction and convection both need particles. |
| A roof is painted shiny white instead of dull black. What is the effect inside the building? | It stays cooler, because the roof reflects more of the Sun's radiation | It becomes hotter, because white absorbs more radiation · There is no change, because the roof is the same material · It stays cooler, because white conducts heat away faster | Dull dark surfaces absorb best; white reflects. · The surface decides how much radiation is absorbed, whatever the material beneath. · The colour changes how much radiation is absorbed, not how well the roof conducts. | Shiny light surfaces reflect radiation, so less of the Sun's energy enters the building. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Two cans of hot water are alike except that one is dull black and the other shiny silver. Which cools faster?

- ◻️ Both cool at the same rate  
  _↳ feedback if chosen: The surfaces differ, so they radiate at different rates._
- ✅ The dull black one, because a dull black surface is a better emitter of radiation
- ◻️ The shiny one, because shiny metal conducts heat away  
  _↳ feedback if chosen: The cans are the same metal; the paint changes how well they emit, not how they conduct._
- ◻️ The dull black one, because black absorbs more heat  
  _↳ feedback if chosen: These cans are hotter than the room, so they are emitting. The answer is right but the reason is not._

Full working after a second miss:

> Both lose heat by conduction and convection alike; the dull black surface emits radiation best.  
> So the answer is The dull black one, because a dull black surface is a better emitter of radiation.  

> Which surface takes in radiation best?

- ◻️ A shiny silver surface  
  _↳ feedback if chosen: A shiny silver surface reflects most of the radiation that falls on it._
- ◻️ A polished glass surface  
  _↳ feedback if chosen: Polished glass reflects and lets radiation through rather than absorbing it._
- ✅ A dull black surface
- ◻️ A white painted surface  
  _↳ feedback if chosen: White reflects much of the radiation._

Full working after a second miss:

> A good absorber is also a good emitter: dull black is best at both.  
> So the answer is A dull black surface.  

> Why can radiation reach the Earth from the Sun?

- ◻️ Space is full of particles that pass it along  
  _↳ feedback if chosen: Space is nearly empty, so there is nothing to pass heat along._
- ◻️ The air between carries it by conduction  
  _↳ feedback if chosen: There is almost no matter between the Sun and the atmosphere to conduct through._
- ◻️ Convection currents cross space  
  _↳ feedback if chosen: Convection needs a fluid to flow; space is very nearly empty._
- ✅ Radiation is electromagnetic waves, which need no material medium

Full working after a second miss:

> Only radiation can cross a vacuum; conduction and convection both need particles.  
> So the answer is Radiation is electromagnetic waves, which need no material medium.  

Sources: heat-transfer (Form 4 Physics syllabus, Term 1: heat transfer by conduction, convection and radiation and their applications)

### `p4-6-radiate-card` · Lesson 6 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Two cans of hot water are alike except that one is dull black and the other shiny silver. Which cools faster? | The dull black one, because a dull black surface is a better emitter of radiation | The shiny one, because shiny metal conducts heat away · Both cool at the same rate · The dull black one, because black absorbs more heat | The cans are the same metal; the paint changes how well they emit, not how they conduct. · The surfaces differ, so they radiate at different rates. · These cans are hotter than the room, so they are emitting. The answer is right but the reason is not. | Both lose heat by conduction and convection alike; the dull black surface emits radiation best. |
| Which surface takes in radiation best? | A dull black surface | A shiny silver surface · A white painted surface · A polished glass surface | A shiny silver surface reflects most of the radiation that falls on it. · White reflects much of the radiation. · Polished glass reflects and lets radiation through rather than absorbing it. | A good absorber is also a good emitter: dull black is best at both. |
| Why can radiation reach the Earth from the Sun? | Radiation is electromagnetic waves, which need no material medium | The air between carries it by conduction · Convection currents cross space · Space is full of particles that pass it along | There is almost no matter between the Sun and the atmosphere to conduct through. · Convection needs a fluid to flow; space is very nearly empty. · Space is nearly empty, so there is nothing to pass heat along. | Only radiation can cross a vacuum; conduction and convection both need particles. |
| A roof is painted shiny white instead of dull black. What is the effect inside the building? | It stays cooler, because the roof reflects more of the Sun's radiation | It becomes hotter, because white absorbs more radiation · There is no change, because the roof is the same material · It stays cooler, because white conducts heat away faster | Dull dark surfaces absorb best; white reflects. · The surface decides how much radiation is absorbed, whatever the material beneath. · The colour changes how much radiation is absorbed, not how well the roof conducts. | Shiny light surfaces reflect radiation, so less of the Sun's energy enters the building. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A roof is painted shiny white instead of dull black. What is the effect inside the building?

- ◻️ It stays cooler, because white conducts heat away faster  
  _↳ feedback if chosen: The colour changes how much radiation is absorbed, not how well the roof conducts._
- ◻️ There is no change, because the roof is the same material  
  _↳ feedback if chosen: The surface decides how much radiation is absorbed, whatever the material beneath._
- ◻️ It becomes hotter, because white absorbs more radiation  
  _↳ feedback if chosen: Dull dark surfaces absorb best; white reflects._
- ✅ It stays cooler, because the roof reflects more of the Sun's radiation

Full working after a second miss:

> Shiny light surfaces reflect radiation, so less of the Sun's energy enters the building.  
> So the answer is It stays cooler, because the roof reflects more of the Sun's radiation.  

> Which surface takes in radiation best?

- ✅ A dull black surface
- ◻️ A polished glass surface  
  _↳ feedback if chosen: Polished glass reflects and lets radiation through rather than absorbing it._
- ◻️ A white painted surface  
  _↳ feedback if chosen: White reflects much of the radiation._
- ◻️ A shiny silver surface  
  _↳ feedback if chosen: A shiny silver surface reflects most of the radiation that falls on it._

Full working after a second miss:

> A good absorber is also a good emitter: dull black is best at both.  
> So the answer is A dull black surface.  

> Two cans of hot water are alike except that one is dull black and the other shiny silver. Which cools faster?

- ✅ The dull black one, because a dull black surface is a better emitter of radiation
- ◻️ The shiny one, because shiny metal conducts heat away  
  _↳ feedback if chosen: The cans are the same metal; the paint changes how well they emit, not how they conduct._
- ◻️ The dull black one, because black absorbs more heat  
  _↳ feedback if chosen: These cans are hotter than the room, so they are emitting. The answer is right but the reason is not._
- ◻️ Both cool at the same rate  
  _↳ feedback if chosen: The surfaces differ, so they radiate at different rates._

Full working after a second miss:

> Both lose heat by conduction and convection alike; the dull black surface emits radiation best.  
> So the answer is The dull black one, because a dull black surface is a better emitter of radiation.  

Sources: heat-transfer (Form 4 Physics syllabus, Term 1: heat transfer by conduction, convection and radiation and their applications)

### `p4-7-why` · Lesson 7 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does a metal bar get longer when it is heated? | Its particles vibrate more strongly, so they push each other a little further apart | New particles are made inside the metal · The particles themselves get bigger · The metal takes in air as it warms | The number of particles does not change: the same particles take up more room. · A particle does not change size; the spacing between particles grows. · A solid metal bar does not take in air. | Heating gives the particles more energy, so they vibrate more and need more room. |
| Which expands most for the same rise in temperature? | A gas | A solid · A liquid · They all expand by the same amount | A solid expands least: its particles are held tightly in place. · A liquid expands more than a solid but far less than a gas. · The three states expand by very different amounts. | The freer the particles, the more the substance expands: gases most, then liquids, then solids. |
| Why is a small gap left between lengths of railway line? | So that the rails can get longer on a hot day without pushing on each other | To let rain drain away from the track · To make the ride quieter · To save the cost of steel | Drainage is handled by the bed under the track, not by the gaps. · The gaps make the familiar knocking sound; they do not make the ride quieter. · The saving in steel is tiny; the reason is expansion. | Without the gap, expanding rails would push against each other and buckle. |
| A tight metal lid will not turn on a glass jar. Why does holding it under hot water help? | The metal lid expands more than the glass, so it becomes a little looser | The hot water makes the glass contract · The water washes away the dirt holding it · Hot metal becomes softer and bends | The glass is warmed too, and it expands as well, only by less. · Dirt is not usually what holds a lid; the tight fit is. · The lid does not get hot enough to soften. | Metal expands more than glass for the same rise, so the fit between them loosens. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which expands most for the same rise in temperature?

- ◻️ A liquid  
  _↳ feedback if chosen: A liquid expands more than a solid but far less than a gas._
- ◻️ They all expand by the same amount  
  _↳ feedback if chosen: The three states expand by very different amounts._
- ◻️ A solid  
  _↳ feedback if chosen: A solid expands least: its particles are held tightly in place._
- ✅ A gas

Full working after a second miss:

> The freer the particles, the more the substance expands: gases most, then liquids, then solids.  
> So the answer is A gas.  

> Which expands most for the same rise in temperature?

- ◻️ A solid  
  _↳ feedback if chosen: A solid expands least: its particles are held tightly in place._
- ◻️ A liquid  
  _↳ feedback if chosen: A liquid expands more than a solid but far less than a gas._
- ◻️ They all expand by the same amount  
  _↳ feedback if chosen: The three states expand by very different amounts._
- ✅ A gas

Full working after a second miss:

> The freer the particles, the more the substance expands: gases most, then liquids, then solids.  
> So the answer is A gas.  

> Why is a small gap left between lengths of railway line?

- ◻️ To make the ride quieter  
  _↳ feedback if chosen: The gaps make the familiar knocking sound; they do not make the ride quieter._
- ◻️ To let rain drain away from the track  
  _↳ feedback if chosen: Drainage is handled by the bed under the track, not by the gaps._
- ✅ So that the rails can get longer on a hot day without pushing on each other
- ◻️ To save the cost of steel  
  _↳ feedback if chosen: The saving in steel is tiny; the reason is expansion._

Full working after a second miss:

> Without the gap, expanding rails would push against each other and buckle.  
> So the answer is So that the rails can get longer on a hot day without pushing on each other.  

Sources: expansion (Form 4 Physics syllabus, Term 1: thermal expansion, the bimetallic strip and its principles, radiant energy converters)

### `p4-7-bimetal` · Lesson 7 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A bimetallic strip of brass and invar is heated. Which way does it bend? | Towards the invar, with the brass on the outside of the curve | Towards the brass, with the invar on the outside · It stays straight and just gets longer · It bends one way, then the other | Invar expands very little; the side that expands more must take the outside. · The two sides grow by different amounts, so the strip must bend. · It bends one way on heating and the other way on cooling, not both at once. | Brass expands more, and the two are joined, so the brass takes the longer path round the outside. |
| The same brass and invar strip is then cooled well below room temperature. Which way does it bend? | The other way, with the invar on the outside | The same way as when heated · It stays bent as it was · It breaks apart | Cooling contracts the brass more, so the bending is reversed. · The strip returns through the straight shape and then bends the other way. · The two metals are riveted together and stay joined. | Brass contracts more than invar, so now the brass is the shorter side and takes the inside of the curve. |
| How does a bimetallic strip work in a fire alarm? | The heat of a fire bends the strip until it touches a contact and completes the circuit | The strip melts and lets the current through · The strip blocks the current when it is hot · The strip rings the bell by vibrating | The strip does not melt; it bends while staying solid. · In an alarm the strip CLOSES the circuit; a thermostat is the one that breaks it. · The bell is rung by the circuit, not by the strip itself. | Bending on heating closes a gap in the circuit, so the bell rings. |
| How does a bimetallic strip control the temperature of an electric iron? | When the iron gets too hot the strip bends and breaks the circuit, and it closes again as the iron cools | It bends and closes the circuit when the iron is hot · It melts at the chosen temperature · It measures the temperature on a dial only | Closing the circuit when hot would make the iron hotter still. · The strip stays solid; it bends instead of melting. · It does more than show a temperature: it switches the heater off and on. | A thermostat uses the bending to switch the heater off when hot and on again when cool. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How does a bimetallic strip work in a fire alarm?

- ◻️ The strip melts and lets the current through  
  _↳ feedback if chosen: The strip does not melt; it bends while staying solid._
- ◻️ The strip blocks the current when it is hot  
  _↳ feedback if chosen: In an alarm the strip CLOSES the circuit; a thermostat is the one that breaks it._
- ✅ The heat of a fire bends the strip until it touches a contact and completes the circuit
- ◻️ The strip rings the bell by vibrating  
  _↳ feedback if chosen: The bell is rung by the circuit, not by the strip itself._

Full working after a second miss:

> Bending on heating closes a gap in the circuit, so the bell rings.  
> So the answer is The heat of a fire bends the strip until it touches a contact and completes the circuit.  

> A bimetallic strip of brass and invar is heated. Which way does it bend?

- ◻️ It stays straight and just gets longer  
  _↳ feedback if chosen: The two sides grow by different amounts, so the strip must bend._
- ◻️ Towards the brass, with the invar on the outside  
  _↳ feedback if chosen: Invar expands very little; the side that expands more must take the outside._
- ◻️ It bends one way, then the other  
  _↳ feedback if chosen: It bends one way on heating and the other way on cooling, not both at once._
- ✅ Towards the invar, with the brass on the outside of the curve

Full working after a second miss:

> Brass expands more, and the two are joined, so the brass takes the longer path round the outside.  
> So the answer is Towards the invar, with the brass on the outside of the curve.  

> How does a bimetallic strip control the temperature of an electric iron?

- ◻️ It bends and closes the circuit when the iron is hot  
  _↳ feedback if chosen: Closing the circuit when hot would make the iron hotter still._
- ◻️ It measures the temperature on a dial only  
  _↳ feedback if chosen: It does more than show a temperature: it switches the heater off and on._
- ◻️ It melts at the chosen temperature  
  _↳ feedback if chosen: The strip stays solid; it bends instead of melting._
- ✅ When the iron gets too hot the strip bends and breaks the circuit, and it closes again as the iron cools

Full working after a second miss:

> A thermostat uses the bending to switch the heater off when hot and on again when cool.  
> So the answer is When the iron gets too hot the strip bends and breaks the circuit, and it closes again as the iron cools.  

Sources: expansion (Form 4 Physics syllabus, Term 1: thermal expansion, the bimetallic strip and its principles, radiant energy converters)

### `p4-7-water` · Lesson 7 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Water is cooled from {8} °C to {0} °C. What happens to its volume? | It contracts down to {4} °C, then expands from {4} °C to {0} °C | It contracts all the way · It expands all the way · It stays the same | Water is unusual: below {4} °C it expands as it cools. · From {8} °C to {4} °C it contracts in the ordinary way. · Its volume does change; water is densest at {4} °C. | Water is densest at {4} °C, so cooling below that makes it expand again. |
| At what temperature is water at its densest? | {4} °C | {0} °C · {100} °C · −{4} °C | At {0} °C water has already expanded again and is less dense than at {4} °C. · Water is least dense as a liquid near its boiling point. · Water is ice below {0} °C, and ice is less dense than water. | Between {0} °C and {4} °C water behaves unusually; at {4} °C its volume is smallest. |
| Why does ice float on water? | Water expands as it freezes, so ice is less dense than water | Ice is colder, and cold things float · Ice traps air bubbles that lift it · Ice is a solid, and solids always float on their liquids | Temperature alone does not decide floating; density does. · Even clear ice with no bubbles floats. · Most solids sink in their own liquid; water is the unusual one. | The particles take up more room in ice than in water, so ice has the lower density. |
| Why does a pond in a cold country freeze from the top down? | Water at {4} °C is densest and sinks, so the coldest water stays on top and freezes there | The bottom of a pond is always warmer than the air · Ice forms first on the ground and floats up · Cold water is denser, so it freezes at the bottom | The bottom stays near {4} °C because of the unusual density of water, not because of the ground. · Ice forms at the surface, where the water is coldest. · Water below {4} °C is LESS dense, so it stays at the top. | Water cooled below {4} °C rises to the surface, and the ice that forms floats, letting fish live below. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Water is cooled from 8 °C to 0 °C. What happens to its volume?

- ✅ It contracts down to 4 °C, then expands from 4 °C to 0 °C
- ◻️ It stays the same  
  _↳ feedback if chosen: Its volume does change; water is densest at 4 °C._
- ◻️ It expands all the way  
  _↳ feedback if chosen: From 8 °C to 4 °C it contracts in the ordinary way._
- ◻️ It contracts all the way  
  _↳ feedback if chosen: Water is unusual: below 4 °C it expands as it cools._

Full working after a second miss:

> Water is densest at 4 °C, so cooling below that makes it expand again.  
> So the answer is It contracts down to 4 °C, then expands from 4 °C to 0 °C.  

> Why does ice float on water?

- ◻️ Ice is colder, and cold things float  
  _↳ feedback if chosen: Temperature alone does not decide floating; density does._
- ◻️ Ice traps air bubbles that lift it  
  _↳ feedback if chosen: Even clear ice with no bubbles floats._
- ◻️ Ice is a solid, and solids always float on their liquids  
  _↳ feedback if chosen: Most solids sink in their own liquid; water is the unusual one._
- ✅ Water expands as it freezes, so ice is less dense than water

Full working after a second miss:

> The particles take up more room in ice than in water, so ice has the lower density.  
> So the answer is Water expands as it freezes, so ice is less dense than water.  

> Why does ice float on water?

- ◻️ Ice is a solid, and solids always float on their liquids  
  _↳ feedback if chosen: Most solids sink in their own liquid; water is the unusual one._
- ✅ Water expands as it freezes, so ice is less dense than water
- ◻️ Ice traps air bubbles that lift it  
  _↳ feedback if chosen: Even clear ice with no bubbles floats._
- ◻️ Ice is colder, and cold things float  
  _↳ feedback if chosen: Temperature alone does not decide floating; density does._

Full working after a second miss:

> The particles take up more room in ice than in water, so ice has the lower density.  
> So the answer is Water expands as it freezes, so ice is less dense than water.  

Sources: expansion (Form 4 Physics syllabus, Term 1: thermal expansion, the bimetallic strip and its principles, radiant energy converters)

### `p4-8-kind` · Lesson 8 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is a wave? | A travelling disturbance that carries energy without carrying the material along | A flow of matter from one place to another · A store of energy that stays in one place · A kind of force | A cork on water bobs up and down and stays in place, so the water is not carried along. · A wave travels; it does not stay in one place. · A wave carries energy; a force is a push or a pull. | Each particle vibrates about its own position and passes the energy on to the next. |
| Which wave needs a material medium to travel through? | A sound wave | A light wave · A radio wave · An X-ray | Light is electromagnetic and crosses the vacuum of space. · Radio waves are electromagnetic and reach us from satellites through space. · X-rays are electromagnetic and also cross a vacuum. | Sound is mechanical: it needs particles to pass the vibration on, so it cannot cross a vacuum. |
| In a transverse wave, how do the particles move? | At right angles to the direction the wave travels | Along the direction the wave travels · In circles around the source · They do not move at all | That describes a longitudinal wave, such as sound. · The particles vibrate about a fixed position, backwards and forwards or up and down. · The particles do move; it is the wave that carries energy through them. | Water ripples and light are transverse: the vibration is across the direction of travel. |
| In a longitudinal wave, how do the particles move? | Backwards and forwards along the direction the wave travels | At right angles to the direction of travel · They travel along with the wave · They stay completely still | That describes a transverse wave, such as a water ripple. · The particles vibrate about fixed positions; only the energy travels on. · The particles vibrate; otherwise no energy would be passed along. | Sound in air is longitudinal: the air is squeezed into compressions and stretched into rarefactions. |
| Which list contains only mechanical waves? | Sound, water ripples and waves on a spring | Light, radio and X-rays · Sound, light and water ripples · Radio, microwaves and sound | Those three are electromagnetic: they need no medium. · Light is electromagnetic, not mechanical. · Radio and microwaves are electromagnetic. | A mechanical wave needs a medium; sound, water ripples and spring waves all do. |
| A sound wave travels through air. What is a compression? | A region where the air particles are pushed closer together | A region where the particles are further apart than usual · A point where the wave stops · The highest point of the wave | That is a rarefaction, the opposite of a compression. · The wave does not stop; compressions travel along with it. · Highest and lowest points belong to a transverse wave, not to sound in air. | A longitudinal wave is a series of compressions and rarefactions passing through the medium. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is a wave?

- ✅ A travelling disturbance that carries energy without carrying the material along
- ◻️ A flow of matter from one place to another  
  _↳ feedback if chosen: A cork on water bobs up and down and stays in place, so the water is not carried along._
- ◻️ A store of energy that stays in one place  
  _↳ feedback if chosen: A wave travels; it does not stay in one place._
- ◻️ A kind of force  
  _↳ feedback if chosen: A wave carries energy; a force is a push or a pull._

Full working after a second miss:

> Each particle vibrates about its own position and passes the energy on to the next.  
> So the answer is A travelling disturbance that carries energy without carrying the material along.  

> Which wave needs a material medium to travel through?

- ✅ A sound wave
- ◻️ A radio wave  
  _↳ feedback if chosen: Radio waves are electromagnetic and reach us from satellites through space._
- ◻️ A light wave  
  _↳ feedback if chosen: Light is electromagnetic and crosses the vacuum of space._
- ◻️ An X-ray  
  _↳ feedback if chosen: X-rays are electromagnetic and also cross a vacuum._

Full working after a second miss:

> Sound is mechanical: it needs particles to pass the vibration on, so it cannot cross a vacuum.  
> So the answer is A sound wave.  

> Which list contains only mechanical waves?

- ◻️ Radio, microwaves and sound  
  _↳ feedback if chosen: Radio and microwaves are electromagnetic._
- ◻️ Light, radio and X-rays  
  _↳ feedback if chosen: Those three are electromagnetic: they need no medium._
- ✅ Sound, water ripples and waves on a spring
- ◻️ Sound, light and water ripples  
  _↳ feedback if chosen: Light is electromagnetic, not mechanical._

Full working after a second miss:

> A mechanical wave needs a medium; sound, water ripples and spring waves all do.  
> So the answer is Sound, water ripples and waves on a spring.  

Sources: waves (Form 4 Physics syllabus, Term 1: classification of waves by medium and by mode of propagation; wave characteristics (energy transfer, period, frequency, amplitude, wavelength, wave speed); the ripple tank; v = fλ; stationary waves, harmonics and overtones; vibrating strings)

### `p4-8-medium` · Lesson 8 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A ringing electric bell is inside a glass jar and the air is slowly pumped out. What happens? | The sound fades away, but the bell can still be seen ringing | The sound gets louder as the air is removed · Both the sound and the light disappear · Nothing changes | Fewer particles carry less sound, so it gets quieter, not louder. · Light needs no medium: it still passes through the vacuum. · Removing the air removes the medium that the sound needs. | Sound needs particles to pass the vibration on; light is electromagnetic and crosses a vacuum. |
| Two astronauts stand side by side on the Moon, which has no atmosphere. Can they talk to each other directly? | No: there is no air to carry the sound, so they must use radio | Yes, because they are very close together · Yes, because sound travels faster in a vacuum · No, because the Moon is too cold for sound | Distance is not the problem: there is no medium at all. · Sound cannot travel in a vacuum at any speed. · Temperature changes the speed of sound a little, but the real problem is that there is no air. | Sound is mechanical; radio waves are electromagnetic and cross the vacuum. |
| Why can a diver under water hear a boat engine? | Water is a medium, and sound travels through it even faster than through air | Sound travels only through air, so the diver hears it when surfacing · The sound travels through the vacuum between the boat and the diver · Water blocks sound completely | Liquids carry sound well; the diver hears it under water. · There is no vacuum between a boat and a diver; the water is the medium. · Water carries sound better than air does. | A mechanical wave travels through any medium with particles, and faster where they are closer together. |
| Which of these could NOT reach us from a distant star? | The sound of the star | Light from the star · Radio waves from the star · X-rays from the star | Light is electromagnetic and crosses the near-vacuum of space. · Radio waves are electromagnetic and are received by radio telescopes. · X-rays are electromagnetic and are detected by satellites. | Only electromagnetic waves cross space; sound needs a material medium. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Two astronauts stand side by side on the Moon, which has no atmosphere. Can they talk to each other directly?

- ◻️ Yes, because sound travels faster in a vacuum  
  _↳ feedback if chosen: Sound cannot travel in a vacuum at any speed._
- ✅ No: there is no air to carry the sound, so they must use radio
- ◻️ No, because the Moon is too cold for sound  
  _↳ feedback if chosen: Temperature changes the speed of sound a little, but the real problem is that there is no air._
- ◻️ Yes, because they are very close together  
  _↳ feedback if chosen: Distance is not the problem: there is no medium at all._

Full working after a second miss:

> Sound is mechanical; radio waves are electromagnetic and cross the vacuum.  
> So the answer is No: there is no air to carry the sound, so they must use radio.  

> Two astronauts stand side by side on the Moon, which has no atmosphere. Can they talk to each other directly?

- ◻️ Yes, because sound travels faster in a vacuum  
  _↳ feedback if chosen: Sound cannot travel in a vacuum at any speed._
- ✅ No: there is no air to carry the sound, so they must use radio
- ◻️ Yes, because they are very close together  
  _↳ feedback if chosen: Distance is not the problem: there is no medium at all._
- ◻️ No, because the Moon is too cold for sound  
  _↳ feedback if chosen: Temperature changes the speed of sound a little, but the real problem is that there is no air._

Full working after a second miss:

> Sound is mechanical; radio waves are electromagnetic and cross the vacuum.  
> So the answer is No: there is no air to carry the sound, so they must use radio.  

> A ringing electric bell is inside a glass jar and the air is slowly pumped out. What happens?

- ◻️ Both the sound and the light disappear  
  _↳ feedback if chosen: Light needs no medium: it still passes through the vacuum._
- ✅ The sound fades away, but the bell can still be seen ringing
- ◻️ The sound gets louder as the air is removed  
  _↳ feedback if chosen: Fewer particles carry less sound, so it gets quieter, not louder._
- ◻️ Nothing changes  
  _↳ feedback if chosen: Removing the air removes the medium that the sound needs._

Full working after a second miss:

> Sound needs particles to pass the vibration on; light is electromagnetic and crosses a vacuum.  
> So the answer is The sound fades away, but the bell can still be seen ringing.  

Sources: waves (Form 4 Physics syllabus, Term 1: classification of waves by medium and by mode of propagation; wave characteristics (energy transfer, period, frequency, amplitude, wavelength, wave speed); the ripple tank; v = fλ; stationary waves, harmonics and overtones; vibrating strings)

### `p4-8-match` · Lesson 8 · matching, level 2

Prompt: Match each wave to the kind it is.

Pairs (3 shown each time):

- Sound in air → **Mechanical and longitudinal**
- A ripple on water → **Mechanical and transverse**
- Light from the Sun → **Electromagnetic and transverse**
- A wave along a stretched rope → **Mechanical and transverse**
- Radio waves from a mast → **Electromagnetic and transverse**


Three generated variants:

> Match each wave to the kind it is.

Right-hand side (shuffled): Electromagnetic and transverse · Mechanical and transverse · Mechanical and longitudinal
- Radio waves from a mast → **Electromagnetic and transverse**
- Sound in air → **Mechanical and longitudinal**
- A ripple on water → **Mechanical and transverse**

Full working after a second miss:

> The right pairs are:  
> Radio waves from a mast → Electromagnetic and transverse  
> Sound in air → Mechanical and longitudinal  
> A ripple on water → Mechanical and transverse  

> Match each wave to the kind it is.

Right-hand side (shuffled): Mechanical and longitudinal · Electromagnetic and transverse · Mechanical and transverse
- Sound in air → **Mechanical and longitudinal**
- A ripple on water → **Mechanical and transverse**
- Radio waves from a mast → **Electromagnetic and transverse**

Full working after a second miss:

> The right pairs are:  
> Sound in air → Mechanical and longitudinal  
> A ripple on water → Mechanical and transverse  
> Radio waves from a mast → Electromagnetic and transverse  

> Match each wave to the kind it is.

Right-hand side (shuffled): Electromagnetic and transverse · Mechanical and longitudinal · Mechanical and transverse
- A ripple on water → **Mechanical and transverse**
- Radio waves from a mast → **Electromagnetic and transverse**
- Sound in air → **Mechanical and longitudinal**

Full working after a second miss:

> The right pairs are:  
> A ripple on water → Mechanical and transverse  
> Radio waves from a mast → Electromagnetic and transverse  
> Sound in air → Mechanical and longitudinal  

Sources: waves (Form 4 Physics syllabus, Term 1: classification of waves by medium and by mode of propagation; wave characteristics (energy transfer, period, frequency, amplitude, wavelength, wave speed); the ripple tank; v = fλ; stationary waves, harmonics and overtones; vibrating strings)

### `p4-8-energy` · Lesson 8 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A boat rocks as waves pass under it, but it does not travel towards the shore. What does this show? | A wave carries energy along, while the water itself only vibrates about one place | The waves have no energy · The water travels to the shore but the boat does not · The boat is too heavy to be moved by waves | The rocking of the boat shows that energy is arriving. · If the water flowed to the shore, the boat would be carried with it. · A light cork behaves in the same way: it bobs without travelling. | Each part of the water moves up and down and passes the energy to the next part. |
| A loud sound shakes a window pane across the room. What has crossed the room? | Energy, carried by the sound wave through the air | Air blown from the source to the window · Particles shot out by the source · Nothing: the window shakes by itself | The air vibrates in place; it does not blow across the room. · No particles leave the source; the air already there passes the vibration on. · The window shakes only when the sound is made, so something reaches it. | A wave carries energy without carrying the medium along with it. |
| Two waves on a pond have the same wavelength, but one is twice as tall. What does the taller one carry? | More energy, because the energy of a wave grows with its amplitude | Less energy, because it moves more slowly · The same energy, because the wavelength is the same · The same energy, but at a higher frequency | Both travel at the same speed in the same water; height does not slow a wave. · Wavelength is not what decides the energy; amplitude is. · Equal wavelength at equal speed means equal frequency. | A bigger amplitude means a bigger disturbance, and so more energy carried. |
| Sunlight warms a roof. How has the energy reached it? | As an electromagnetic wave, which needs no medium | As hot air blown from the Sun · As a mechanical wave through space · By conduction along the atmosphere | No air travels from the Sun; space between is nearly empty. · A mechanical wave needs particles, and space has almost none. · There is nothing between the Sun and the atmosphere to conduct along. | Light is a wave that carries energy across a vacuum. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Two waves on a pond have the same wavelength, but one is twice as tall. What does the taller one carry?

- ◻️ The same energy, because the wavelength is the same  
  _↳ feedback if chosen: Wavelength is not what decides the energy; amplitude is._
- ◻️ The same energy, but at a higher frequency  
  _↳ feedback if chosen: Equal wavelength at equal speed means equal frequency._
- ✅ More energy, because the energy of a wave grows with its amplitude
- ◻️ Less energy, because it moves more slowly  
  _↳ feedback if chosen: Both travel at the same speed in the same water; height does not slow a wave._

Full working after a second miss:

> A bigger amplitude means a bigger disturbance, and so more energy carried.  
> So the answer is More energy, because the energy of a wave grows with its amplitude.  

> Two waves on a pond have the same wavelength, but one is twice as tall. What does the taller one carry?

- ✅ More energy, because the energy of a wave grows with its amplitude
- ◻️ Less energy, because it moves more slowly  
  _↳ feedback if chosen: Both travel at the same speed in the same water; height does not slow a wave._
- ◻️ The same energy, because the wavelength is the same  
  _↳ feedback if chosen: Wavelength is not what decides the energy; amplitude is._
- ◻️ The same energy, but at a higher frequency  
  _↳ feedback if chosen: Equal wavelength at equal speed means equal frequency._

Full working after a second miss:

> A bigger amplitude means a bigger disturbance, and so more energy carried.  
> So the answer is More energy, because the energy of a wave grows with its amplitude.  

> A loud sound shakes a window pane across the room. What has crossed the room?

- ◻️ Nothing: the window shakes by itself  
  _↳ feedback if chosen: The window shakes only when the sound is made, so something reaches it._
- ✅ Energy, carried by the sound wave through the air
- ◻️ Particles shot out by the source  
  _↳ feedback if chosen: No particles leave the source; the air already there passes the vibration on._
- ◻️ Air blown from the source to the window  
  _↳ feedback if chosen: The air vibrates in place; it does not blow across the room._

Full working after a second miss:

> A wave carries energy without carrying the medium along with it.  
> So the answer is Energy, carried by the sound wave through the air.  

Sources: waves (Form 4 Physics syllabus, Term 1: classification of waves by medium and by mode of propagation; wave characteristics (energy transfer, period, frequency, amplitude, wavelength, wave speed); the ripple tank; v = fλ; stationary waves, harmonics and overtones; vibrating strings)

### `p4-11-which` · Lesson 11 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Straight water waves hit a straight barrier at an angle. What happens? | They are reflected, with the angle of reflection equal to the angle of incidence | They pass straight through the barrier · They stop at the barrier and disappear · They bend around the barrier and carry on | A solid barrier does not let the waves through. · The energy is turned back, not destroyed. · Bending round an obstacle is diffraction, which needs a gap or an edge, not a long straight barrier. | At a reflection the wavelength and frequency stay the same; only the direction changes. |
| Water waves pass from deep water into shallow water. What happens to them? | They slow down, the wavelength gets shorter and they bend towards the normal | They speed up and the wavelength gets longer · The frequency changes but the speed does not · Nothing changes | Waves travel more slowly in shallow water, not faster. · The frequency is set by the source and does not change; the speed does. · The change of depth changes the speed, so something must change. | Refraction: f stays the same, v falls, so λ = v ÷ f falls too, and the waves bend. |
| What is diffraction? | The spreading of waves as they pass through a gap or around an obstacle | The bouncing of waves off a barrier · The bending of waves when their speed changes · The joining of two waves to make a bigger one | That is reflection. · That is refraction. · That is interference. | Diffraction spreads the wave; it is greatest when the gap is about the same size as the wavelength. |
| When is diffraction through a gap greatest? | When the width of the gap is about the same as the wavelength | When the gap is much wider than the wavelength · When the gap is much narrower than the wavelength · The width of the gap makes no difference | A wide gap lets most of the wave through almost straight, with only the edges spreading. · A very narrow gap lets through little energy, though what passes does spread. · The width of the gap compared with the wavelength is exactly what decides it. | Gap ≈ wavelength gives the widest spreading, which is why sound (long waves) bends round a doorway but light does not. |
| Two waves meet crest to crest. What happens at that point? | Constructive interference: the displacements add, making a bigger wave | Destructive interference: they cancel out · The waves bounce off each other · The waves stop | Cancelling happens when a crest meets a trough. · Waves pass through each other; they do not bounce off each other. · After meeting, each wave carries on as before. | Where two crests meet, the displacements add: that is constructive interference. |
| Two identical waves meet crest to trough. What is heard or seen at that point? | Destructive interference: they cancel, giving a quiet or dark point | A louder sound or a brighter light · No change at all · The waves change frequency | Louder or brighter is constructive interference, where crest meets crest. · A crest meeting an equal trough gives zero displacement, which is a definite change. · Interference does not change the frequency of either wave. | Equal and opposite displacements add to zero: a quiet point in sound, a dark fringe in light. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Straight water waves hit a straight barrier at an angle. What happens?

- ◻️ They stop at the barrier and disappear  
  _↳ feedback if chosen: The energy is turned back, not destroyed._
- ✅ They are reflected, with the angle of reflection equal to the angle of incidence
- ◻️ They pass straight through the barrier  
  _↳ feedback if chosen: A solid barrier does not let the waves through._
- ◻️ They bend around the barrier and carry on  
  _↳ feedback if chosen: Bending round an obstacle is diffraction, which needs a gap or an edge, not a long straight barrier._

Full working after a second miss:

> At a reflection the wavelength and frequency stay the same; only the direction changes.  
> So the answer is They are reflected, with the angle of reflection equal to the angle of incidence.  

> When is diffraction through a gap greatest?

- ◻️ When the gap is much narrower than the wavelength  
  _↳ feedback if chosen: A very narrow gap lets through little energy, though what passes does spread._
- ◻️ The width of the gap makes no difference  
  _↳ feedback if chosen: The width of the gap compared with the wavelength is exactly what decides it._
- ✅ When the width of the gap is about the same as the wavelength
- ◻️ When the gap is much wider than the wavelength  
  _↳ feedback if chosen: A wide gap lets most of the wave through almost straight, with only the edges spreading._

Full working after a second miss:

> Gap ≈ wavelength gives the widest spreading, which is why sound (long waves) bends round a doorway but light does not.  
> So the answer is When the width of the gap is about the same as the wavelength.  

> What is diffraction?

- ◻️ The bending of waves when their speed changes  
  _↳ feedback if chosen: That is refraction._
- ◻️ The joining of two waves to make a bigger one  
  _↳ feedback if chosen: That is interference._
- ◻️ The bouncing of waves off a barrier  
  _↳ feedback if chosen: That is reflection._
- ✅ The spreading of waves as they pass through a gap or around an obstacle

Full working after a second miss:

> Diffraction spreads the wave; it is greatest when the gap is about the same size as the wavelength.  
> So the answer is The spreading of waves as they pass through a gap or around an obstacle.  

Sources: wave-phenomena (Form 4 Physics syllabus, Term 1: wave phenomena, reflection, refraction, diffraction and interference)

### `p4-11-diffract` · Lesson 11 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why can you hear someone talking round the corner of a corridor, but not see them? | Sound has a wavelength about the size of the opening, so it diffracts strongly; light's wavelength is far smaller | Sound travels faster than light · Light is absorbed by the wall but sound is not · Sound waves are longitudinal and light waves are not | Light travels nearly a million times faster than sound; speed is not what decides diffraction. · Both are stopped by a solid wall; the difference is how much each spreads at the corner. · Transverse waves diffract too: water ripples are transverse and diffract well. | Diffraction is greatest when the gap or obstacle is about the size of the wavelength. |
| Straight water waves pass through a gap much wider than their wavelength. What is seen beyond the gap? | The waves go through almost straight, with a little spreading only at the edges | The waves spread out in a wide semicircle · The waves stop at the gap · The waves change their wavelength | Wide spreading needs a gap about the size of the wavelength. · The waves pass through; the barrier only blocks what hits it. · Diffraction changes the shape of the wavefronts, not the wavelength. | A wide gap diffracts little; the spreading grows as the gap narrows towards one wavelength. |
| The gap in a ripple tank barrier is narrowed until it is about one wavelength wide. What happens to the ripples beyond it? | They spread out in almost semicircular wavefronts | They keep their straight shape · They are reflected back · They travel faster | Straight wavefronts pass a wide gap; a narrow gap spreads them. · The part that hits the barrier is reflected, but what goes through the gap spreads out. · The depth is unchanged, so the speed is unchanged. | Gap ≈ wavelength gives the widest diffraction, and the gap acts almost like a new source. |
| Why does a radio with long waves work better than a television behind a hill? | The longer radio waves diffract round the hill, while the shorter television waves do not | Radio waves are stronger than television waves · Television waves are absorbed by soil · Radio waves travel faster than television waves | Strength is not what decides it; the wavelength compared with the obstacle is. · Both are reflected and absorbed at a hill; it is the diffraction that differs. · All electromagnetic waves travel at the same speed in air. | An obstacle diffracts a wave most when the wavelength is comparable with its size. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why can you hear someone talking round the corner of a corridor, but not see them?

- ◻️ Light is absorbed by the wall but sound is not  
  _↳ feedback if chosen: Both are stopped by a solid wall; the difference is how much each spreads at the corner._
- ◻️ Sound waves are longitudinal and light waves are not  
  _↳ feedback if chosen: Transverse waves diffract too: water ripples are transverse and diffract well._
- ◻️ Sound travels faster than light  
  _↳ feedback if chosen: Light travels nearly a million times faster than sound; speed is not what decides diffraction._
- ✅ Sound has a wavelength about the size of the opening, so it diffracts strongly; light's wavelength is far smaller

Full working after a second miss:

> Diffraction is greatest when the gap or obstacle is about the size of the wavelength.  
> So the answer is Sound has a wavelength about the size of the opening, so it diffracts strongly; light's wavelength is far smaller.  

> The gap in a ripple tank barrier is narrowed until it is about one wavelength wide. What happens to the ripples beyond it?

- ◻️ They travel faster  
  _↳ feedback if chosen: The depth is unchanged, so the speed is unchanged._
- ◻️ They are reflected back  
  _↳ feedback if chosen: The part that hits the barrier is reflected, but what goes through the gap spreads out._
- ✅ They spread out in almost semicircular wavefronts
- ◻️ They keep their straight shape  
  _↳ feedback if chosen: Straight wavefronts pass a wide gap; a narrow gap spreads them._

Full working after a second miss:

> Gap ≈ wavelength gives the widest diffraction, and the gap acts almost like a new source.  
> So the answer is They spread out in almost semicircular wavefronts.  

> Why does a radio with long waves work better than a television behind a hill?

- ◻️ Radio waves travel faster than television waves  
  _↳ feedback if chosen: All electromagnetic waves travel at the same speed in air._
- ◻️ Radio waves are stronger than television waves  
  _↳ feedback if chosen: Strength is not what decides it; the wavelength compared with the obstacle is._
- ✅ The longer radio waves diffract round the hill, while the shorter television waves do not
- ◻️ Television waves are absorbed by soil  
  _↳ feedback if chosen: Both are reflected and absorbed at a hill; it is the diffraction that differs._

Full working after a second miss:

> An obstacle diffracts a wave most when the wavelength is comparable with its size.  
> So the answer is The longer radio waves diffract round the hill, while the shorter television waves do not.  

Sources: wave-phenomena (Form 4 Physics syllabus, Term 1: wave phenomena, reflection, refraction, diffraction and interference)

### `p4-11-interfere` · Lesson 11 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Two loudspeakers play the same steady note. Walking in front of them, a pupil hears loud and quiet places. Why? | The two sound waves interfere: crest on crest gives a loud place, crest on trough a quiet one | One speaker is louder than the other · The sound is reflected off the walls only · The speakers change frequency as the pupil walks | A louder speaker would make one side louder everywhere, not give a pattern of places. · The pattern is heard outdoors too, where there is little echo. · The note is steady; it is the difference in path length that changes as the pupil moves. | Sound from the two speakers travels different distances to each point, so it arrives in step or out of step. |
| At a point, a crest from one wave arrives together with a crest from another. What happens there? | Constructive interference: the displacements add, giving a bigger disturbance | Destructive interference: they cancel out · The waves bounce off each other · The waves stop | Cancelling happens when a crest meets a trough. · Waves pass through each other; they do not bounce off each other. · After meeting, each wave carries on as before. | Where two waves arrive in step, their displacements add. |
| Two identical waves arrive at a point exactly out of step, crest meeting trough. What is observed? | Destructive interference: they cancel, giving a quiet or dark point | A louder sound or a brighter light · No change at all · The waves change frequency | Louder or brighter is constructive interference, crest on crest. · A crest meeting an equal trough gives zero displacement, which is a definite change. · Interference does not change the frequency of either wave. | Equal and opposite displacements add to zero. |
| What must be true of two sources if a steady interference pattern is to be seen? | They must have the same frequency and keep a steady phase relationship | They must have different frequencies · They must be at the same point · They must face in opposite directions | Different frequencies make a pattern that changes all the time, so nothing steady is seen. · Two sources at the same point cannot give different path lengths. · The direction they face does not decide whether the waves interfere. | Sources with the same frequency and a steady phase relationship are called coherent. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Two identical waves arrive at a point exactly out of step, crest meeting trough. What is observed?

- ◻️ The waves change frequency  
  _↳ feedback if chosen: Interference does not change the frequency of either wave._
- ◻️ No change at all  
  _↳ feedback if chosen: A crest meeting an equal trough gives zero displacement, which is a definite change._
- ✅ Destructive interference: they cancel, giving a quiet or dark point
- ◻️ A louder sound or a brighter light  
  _↳ feedback if chosen: Louder or brighter is constructive interference, crest on crest._

Full working after a second miss:

> Equal and opposite displacements add to zero.  
> So the answer is Destructive interference: they cancel, giving a quiet or dark point.  

> Two identical waves arrive at a point exactly out of step, crest meeting trough. What is observed?

- ◻️ No change at all  
  _↳ feedback if chosen: A crest meeting an equal trough gives zero displacement, which is a definite change._
- ◻️ A louder sound or a brighter light  
  _↳ feedback if chosen: Louder or brighter is constructive interference, crest on crest._
- ✅ Destructive interference: they cancel, giving a quiet or dark point
- ◻️ The waves change frequency  
  _↳ feedback if chosen: Interference does not change the frequency of either wave._

Full working after a second miss:

> Equal and opposite displacements add to zero.  
> So the answer is Destructive interference: they cancel, giving a quiet or dark point.  

> Two loudspeakers play the same steady note. Walking in front of them, a pupil hears loud and quiet places. Why?

- ✅ The two sound waves interfere: crest on crest gives a loud place, crest on trough a quiet one
- ◻️ The speakers change frequency as the pupil walks  
  _↳ feedback if chosen: The note is steady; it is the difference in path length that changes as the pupil moves._
- ◻️ One speaker is louder than the other  
  _↳ feedback if chosen: A louder speaker would make one side louder everywhere, not give a pattern of places._
- ◻️ The sound is reflected off the walls only  
  _↳ feedback if chosen: The pattern is heard outdoors too, where there is little echo._

Full working after a second miss:

> Sound from the two speakers travels different distances to each point, so it arrives in step or out of step.  
> So the answer is The two sound waves interfere: crest on crest gives a loud place, crest on trough a quiet one.  

Sources: wave-phenomena (Form 4 Physics syllabus, Term 1: wave phenomena, reflection, refraction, diffraction and interference)

### `p4-11-match` · Lesson 11 · matching, level 3

Prompt: Match each effect to what happens to the wave.

Pairs (3 shown each time):

- Reflection → **The wave is turned back; λ, f and v stay the same**
- Refraction → **The speed changes, so λ changes and the wave bends**
- Diffraction → **The wave spreads out through a gap or round an obstacle**
- Constructive interference → **Two crests meet and the displacements add**
- Destructive interference → **A crest meets a trough and they cancel**


Three generated variants:

> Match each effect to what happens to the wave.

Right-hand side (shuffled): The wave is turned back; λ, f and v stay the same · Two crests meet and the displacements add · The wave spreads out through a gap or round an obstacle
- Constructive interference → **Two crests meet and the displacements add**
- Diffraction → **The wave spreads out through a gap or round an obstacle**
- Reflection → **The wave is turned back; λ, f and v stay the same**

Full working after a second miss:

> The right pairs are:  
> Constructive interference → Two crests meet and the displacements add  
> Diffraction → The wave spreads out through a gap or round an obstacle  
> Reflection → The wave is turned back; λ, f and v stay the same  

> Match each effect to what happens to the wave.

Right-hand side (shuffled): The speed changes, so λ changes and the wave bends · The wave is turned back; λ, f and v stay the same · The wave spreads out through a gap or round an obstacle
- Reflection → **The wave is turned back; λ, f and v stay the same**
- Refraction → **The speed changes, so λ changes and the wave bends**
- Diffraction → **The wave spreads out through a gap or round an obstacle**

Full working after a second miss:

> The right pairs are:  
> Reflection → The wave is turned back; λ, f and v stay the same  
> Refraction → The speed changes, so λ changes and the wave bends  
> Diffraction → The wave spreads out through a gap or round an obstacle  

> Match each effect to what happens to the wave.

Right-hand side (shuffled): A crest meets a trough and they cancel · The speed changes, so λ changes and the wave bends · The wave is turned back; λ, f and v stay the same
- Refraction → **The speed changes, so λ changes and the wave bends**
- Reflection → **The wave is turned back; λ, f and v stay the same**
- Destructive interference → **A crest meets a trough and they cancel**

Full working after a second miss:

> The right pairs are:  
> Refraction → The speed changes, so λ changes and the wave bends  
> Reflection → The wave is turned back; λ, f and v stay the same  
> Destructive interference → A crest meets a trough and they cancel  

Sources: wave-phenomena (Form 4 Physics syllabus, Term 1: wave phenomena, reflection, refraction, diffraction and interference)

### `p4-11-diffract-card` · Lesson 11 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why can you hear someone talking round the corner of a corridor, but not see them? | Sound has a wavelength about the size of the opening, so it diffracts strongly; light's wavelength is far smaller | Sound travels faster than light · Light is absorbed by the wall but sound is not · Sound waves are longitudinal and light waves are not | Light travels nearly a million times faster than sound; speed is not what decides diffraction. · Both are stopped by a solid wall; the difference is how much each spreads at the corner. · Transverse waves diffract too: water ripples are transverse and diffract well. | Diffraction is greatest when the gap or obstacle is about the size of the wavelength. |
| Straight water waves pass through a gap much wider than their wavelength. What is seen beyond the gap? | The waves go through almost straight, with a little spreading only at the edges | The waves spread out in a wide semicircle · The waves stop at the gap · The waves change their wavelength | Wide spreading needs a gap about the size of the wavelength. · The waves pass through; the barrier only blocks what hits it. · Diffraction changes the shape of the wavefronts, not the wavelength. | A wide gap diffracts little; the spreading grows as the gap narrows towards one wavelength. |
| The gap in a ripple tank barrier is narrowed until it is about one wavelength wide. What happens to the ripples beyond it? | They spread out in almost semicircular wavefronts | They keep their straight shape · They are reflected back · They travel faster | Straight wavefronts pass a wide gap; a narrow gap spreads them. · The part that hits the barrier is reflected, but what goes through the gap spreads out. · The depth is unchanged, so the speed is unchanged. | Gap ≈ wavelength gives the widest diffraction, and the gap acts almost like a new source. |
| Why does a radio with long waves work better than a television behind a hill? | The longer radio waves diffract round the hill, while the shorter television waves do not | Radio waves are stronger than television waves · Television waves are absorbed by soil · Radio waves travel faster than television waves | Strength is not what decides it; the wavelength compared with the obstacle is. · Both are reflected and absorbed at a hill; it is the diffraction that differs. · All electromagnetic waves travel at the same speed in air. | An obstacle diffracts a wave most when the wavelength is comparable with its size. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Straight water waves pass through a gap much wider than their wavelength. What is seen beyond the gap?

- ✅ The waves go through almost straight, with a little spreading only at the edges
- ◻️ The waves change their wavelength  
  _↳ feedback if chosen: Diffraction changes the shape of the wavefronts, not the wavelength._
- ◻️ The waves stop at the gap  
  _↳ feedback if chosen: The waves pass through; the barrier only blocks what hits it._
- ◻️ The waves spread out in a wide semicircle  
  _↳ feedback if chosen: Wide spreading needs a gap about the size of the wavelength._

Full working after a second miss:

> A wide gap diffracts little; the spreading grows as the gap narrows towards one wavelength.  
> So the answer is The waves go through almost straight, with a little spreading only at the edges.  

> The gap in a ripple tank barrier is narrowed until it is about one wavelength wide. What happens to the ripples beyond it?

- ◻️ They keep their straight shape  
  _↳ feedback if chosen: Straight wavefronts pass a wide gap; a narrow gap spreads them._
- ◻️ They travel faster  
  _↳ feedback if chosen: The depth is unchanged, so the speed is unchanged._
- ✅ They spread out in almost semicircular wavefronts
- ◻️ They are reflected back  
  _↳ feedback if chosen: The part that hits the barrier is reflected, but what goes through the gap spreads out._

Full working after a second miss:

> Gap ≈ wavelength gives the widest diffraction, and the gap acts almost like a new source.  
> So the answer is They spread out in almost semicircular wavefronts.  

> The gap in a ripple tank barrier is narrowed until it is about one wavelength wide. What happens to the ripples beyond it?

- ✅ They spread out in almost semicircular wavefronts
- ◻️ They keep their straight shape  
  _↳ feedback if chosen: Straight wavefronts pass a wide gap; a narrow gap spreads them._
- ◻️ They are reflected back  
  _↳ feedback if chosen: The part that hits the barrier is reflected, but what goes through the gap spreads out._
- ◻️ They travel faster  
  _↳ feedback if chosen: The depth is unchanged, so the speed is unchanged._

Full working after a second miss:

> Gap ≈ wavelength gives the widest diffraction, and the gap acts almost like a new source.  
> So the answer is They spread out in almost semicircular wavefronts.  

Sources: wave-phenomena (Form 4 Physics syllabus, Term 1: wave phenomena, reflection, refraction, diffraction and interference)

### `p4-12-compare` · Lesson 12 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How does a stationary wave differ from a progressive wave? | A stationary wave has fixed nodes and carries no energy along; a progressive wave carries energy forward | A stationary wave has a higher frequency · A stationary wave has no amplitude · There is no difference; the names mean the same thing | The two waves that make a stationary wave have the same frequency as it does. · The antinodes have a large amplitude; only the nodes do not move. · They behave quite differently: one carries energy away, the other does not. | In a stationary wave the pattern stays where it is, with the energy stored in the vibration. |
| What is needed to make a stationary wave? | Two waves of the same frequency and amplitude travelling in opposite directions | Two waves of different frequencies travelling the same way · One wave of very large amplitude · Two waves travelling the same way at different speeds | Different frequencies give a pattern that will not stay still. · A single wave travelling along is a progressive wave, however large. · Waves going the same way cannot make fixed nodes. | Usually a wave and its own reflection meet and interfere, giving fixed nodes and antinodes. |
| In a stationary wave, how does the amplitude vary along the string? | It is zero at the nodes and greatest at the antinodes | It is the same everywhere, as in a progressive wave · It is greatest at the nodes · It falls steadily from one end to the other | Equal amplitude everywhere is what happens in a progressive wave. · A node is a point that never moves, so its amplitude is zero. · The amplitude rises and falls repeatedly along the string. | Nodes are points of destructive interference and antinodes points of constructive interference. |
| Why does a stationary wave on a string carry no energy along the string? | The nodes never move, so no energy can pass through them | The string is too short to carry energy · The energy is destroyed at the nodes · The wave has no amplitude anywhere | Length is not the reason; a long string behaves the same way. · Energy is never destroyed; here it stays stored in the vibrating loops. · The antinodes vibrate with a large amplitude. | Energy is stored in each loop, moving between kinetic and potential, but it does not travel past a node. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does a stationary wave on a string carry no energy along the string?

- ◻️ The wave has no amplitude anywhere  
  _↳ feedback if chosen: The antinodes vibrate with a large amplitude._
- ✅ The nodes never move, so no energy can pass through them
- ◻️ The energy is destroyed at the nodes  
  _↳ feedback if chosen: Energy is never destroyed; here it stays stored in the vibrating loops._
- ◻️ The string is too short to carry energy  
  _↳ feedback if chosen: Length is not the reason; a long string behaves the same way._

Full working after a second miss:

> Energy is stored in each loop, moving between kinetic and potential, but it does not travel past a node.  
> So the answer is The nodes never move, so no energy can pass through them.  

> How does a stationary wave differ from a progressive wave?

- ◻️ A stationary wave has a higher frequency  
  _↳ feedback if chosen: The two waves that make a stationary wave have the same frequency as it does._
- ✅ A stationary wave has fixed nodes and carries no energy along; a progressive wave carries energy forward
- ◻️ A stationary wave has no amplitude  
  _↳ feedback if chosen: The antinodes have a large amplitude; only the nodes do not move._
- ◻️ There is no difference; the names mean the same thing  
  _↳ feedback if chosen: They behave quite differently: one carries energy away, the other does not._

Full working after a second miss:

> In a stationary wave the pattern stays where it is, with the energy stored in the vibration.  
> So the answer is A stationary wave has fixed nodes and carries no energy along; a progressive wave carries energy forward.  

> In a stationary wave, how does the amplitude vary along the string?

- ✅ It is zero at the nodes and greatest at the antinodes
- ◻️ It is greatest at the nodes  
  _↳ feedback if chosen: A node is a point that never moves, so its amplitude is zero._
- ◻️ It falls steadily from one end to the other  
  _↳ feedback if chosen: The amplitude rises and falls repeatedly along the string._
- ◻️ It is the same everywhere, as in a progressive wave  
  _↳ feedback if chosen: Equal amplitude everywhere is what happens in a progressive wave._

Full working after a second miss:

> Nodes are points of destructive interference and antinodes points of constructive interference.  
> So the answer is It is zero at the nodes and greatest at the antinodes.  

Sources: waves (Form 4 Physics syllabus, Term 1: classification of waves by medium and by mode of propagation; wave characteristics (energy transfer, period, frequency, amplitude, wavelength, wave speed); the ripple tank; v = fλ; stationary waves, harmonics and overtones; vibrating strings)

### `p4-13-which` · Lesson 13 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What produces a sound? | A vibrating object | A hot object · A moving object of any kind · A bright object | Heat alone makes no sound; a hot stone is silent. · An object can move smoothly and silently; it is vibration that makes sound. · Light and sound are different; a lamp is silent. | Every source of sound vibrates: a drum skin, a string, vocal cords, a loudspeaker cone. |
| How does a sound wave travel through air? | As compressions and rarefactions passing through the air | As crests and troughs of the air moving sideways · By the air itself blowing from the source to the ear · As a beam of particles shot out by the source | Crests and troughs belong to a transverse wave; sound in air is longitudinal. · The air does not travel from the source to the ear; it vibrates in place. · No particles are shot out; the existing air passes the vibration on. | The vibrating source pushes the air into compressions and leaves rarefactions between them. |
| Two notes have the same loudness but one sounds higher. What differs? | The frequency: the higher note has the greater frequency | The amplitude · The speed of the sound in air · The wavelength only, with the frequency unchanged | Amplitude decides loudness, which is said to be the same here. · All sounds travel at the same speed in the same air. · If the speed is fixed and the wavelength changes, the frequency changes too. | Pitch depends on frequency: more vibrations each second gives a higher note. |
| Two notes have the same pitch but one is louder. What differs? | The amplitude: the louder note has the greater amplitude | The frequency · The speed in air · The quality only | Equal pitch means equal frequency. · The speed in the same air is the same for both. · Quality is about the mixture of overtones, not about loudness. | Loudness depends on amplitude, which is the energy the wave carries. |
| The same note is played on a flute and on a guitar, and they sound different. What is this difference called? | Quality (timbre), caused by the mixture of overtones | Pitch · Loudness · Speed | The pitch is the same: both play the same note. · They can be played equally loudly and still sound different. · Both sounds travel at the same speed in air. | Each instrument produces the fundamental with a different mixture of overtones, and that mixture is its quality. |
| Through which does sound travel fastest? | A steel rail | Air · Water · A vacuum | Sound travels slowest of these in air, about {340} m/s. · Sound travels faster in water than in air, but faster still in a solid. · Sound cannot travel through a vacuum at all. | The particles of a solid are closest together, so they pass the vibration on fastest. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Through which does sound travel fastest?

- ✅ A steel rail
- ◻️ Water  
  _↳ feedback if chosen: Sound travels faster in water than in air, but faster still in a solid._
- ◻️ A vacuum  
  _↳ feedback if chosen: Sound cannot travel through a vacuum at all._
- ◻️ Air  
  _↳ feedback if chosen: Sound travels slowest of these in air, about 340 m/s._

Full working after a second miss:

> The particles of a solid are closest together, so they pass the vibration on fastest.  
> So the answer is A steel rail.  

> What produces a sound?

- ◻️ A moving object of any kind  
  _↳ feedback if chosen: An object can move smoothly and silently; it is vibration that makes sound._
- ◻️ A hot object  
  _↳ feedback if chosen: Heat alone makes no sound; a hot stone is silent._
- ✅ A vibrating object
- ◻️ A bright object  
  _↳ feedback if chosen: Light and sound are different; a lamp is silent._

Full working after a second miss:

> Every source of sound vibrates: a drum skin, a string, vocal cords, a loudspeaker cone.  
> So the answer is A vibrating object.  

> Two notes have the same pitch but one is louder. What differs?

- ◻️ The quality only  
  _↳ feedback if chosen: Quality is about the mixture of overtones, not about loudness._
- ◻️ The frequency  
  _↳ feedback if chosen: Equal pitch means equal frequency._
- ✅ The amplitude: the louder note has the greater amplitude
- ◻️ The speed in air  
  _↳ feedback if chosen: The speed in the same air is the same for both._

Full working after a second miss:

> Loudness depends on amplitude, which is the energy the wave carries.  
> So the answer is The amplitude: the louder note has the greater amplitude.  

Sources: sound (Form 4 Physics syllabus, Term 1: production and transmission of sound; characteristics of sound; measurement of the speed of sound by the echo and gun-firing methods; application of echo in sea bed depth)

### `p4-13-quality` · Lesson 13 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| The same note is played on a guitar and on a flute, equally loudly. Which statement is true? | They have the same pitch and loudness but different quality, because of their different overtones | They have different pitches · The flute sound travels faster · They are identical sounds | Playing 'the same note' means the same fundamental frequency, so the pitch is the same. · All sounds travel at the same speed in the same air. · They are easy to tell apart, which is why quality is a separate characteristic. | Each instrument adds its own mixture of overtones to the fundamental, and that mixture is its quality. |
| What makes one person's voice sound different from another's, even on the same note? | The mixture of overtones each voice produces, which is its quality | The speed of the sound each makes · The pitch of the note · The loudness of the voice | All voices travel at the same speed in the same air. · Singing the same note means the same pitch for both. · Both can sing equally loudly and still sound different. | Quality, or timbre, comes from the overtones present along with the fundamental. |
| A tuning fork and a violin both sound a note of {256} Hz. Why does the fork sound plainer? | A tuning fork gives almost only the fundamental, with few overtones | A tuning fork is quieter · A tuning fork gives a higher pitch · A tuning fork makes a longitudinal wave and the violin a transverse one | A fork can be struck hard and still sound plain. · Both sound {256} Hz, so the pitch is the same. · Both make longitudinal sound waves in the air. | A nearly pure note has little beyond the fundamental; the extra overtones of a violin give it a richer quality. |
| Which characteristic of a sound depends on the amplitude of the wave? | Its loudness | Its pitch · Its quality · Its speed | Pitch depends on the frequency. · Quality depends on the mixture of overtones. · The speed depends on the medium, not on the wave's amplitude. | A larger amplitude carries more energy, and the sound is louder. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which characteristic of a sound depends on the amplitude of the wave?

- ◻️ Its speed  
  _↳ feedback if chosen: The speed depends on the medium, not on the wave's amplitude._
- ◻️ Its pitch  
  _↳ feedback if chosen: Pitch depends on the frequency._
- ✅ Its loudness
- ◻️ Its quality  
  _↳ feedback if chosen: Quality depends on the mixture of overtones._

Full working after a second miss:

> A larger amplitude carries more energy, and the sound is louder.  
> So the answer is Its loudness.  

> The same note is played on a guitar and on a flute, equally loudly. Which statement is true?

- ✅ They have the same pitch and loudness but different quality, because of their different overtones
- ◻️ They are identical sounds  
  _↳ feedback if chosen: They are easy to tell apart, which is why quality is a separate characteristic._
- ◻️ The flute sound travels faster  
  _↳ feedback if chosen: All sounds travel at the same speed in the same air._
- ◻️ They have different pitches  
  _↳ feedback if chosen: Playing 'the same note' means the same fundamental frequency, so the pitch is the same._

Full working after a second miss:

> Each instrument adds its own mixture of overtones to the fundamental, and that mixture is its quality.  
> So the answer is They have the same pitch and loudness but different quality, because of their different overtones.  

> Which characteristic of a sound depends on the amplitude of the wave?

- ◻️ Its pitch  
  _↳ feedback if chosen: Pitch depends on the frequency._
- ◻️ Its quality  
  _↳ feedback if chosen: Quality depends on the mixture of overtones._
- ◻️ Its speed  
  _↳ feedback if chosen: The speed depends on the medium, not on the wave's amplitude._
- ✅ Its loudness

Full working after a second miss:

> A larger amplitude carries more energy, and the sound is louder.  
> So the answer is Its loudness.  

Sources: sound (Form 4 Physics syllabus, Term 1: production and transmission of sound; characteristics of sound; measurement of the speed of sound by the echo and gun-firing methods; application of echo in sea bed depth)

### `p4-13-medium` · Lesson 13 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A pupil puts an ear to a long steel rail and a friend taps the far end once. What is heard? | Two sounds: the one through the steel first, then the one through the air | Only one sound, through the air · Only one sound, through the steel · No sound at all | The rail carries sound too, and faster than the air does. · The air also carries the sound, arriving a little later. · Both the steel and the air are media that carry sound. | Sound travels much faster in a solid, where the particles are closest together. |
| In which does sound travel fastest? | In a steel bar | In air · In water · In a vacuum | Sound is slowest of these in air, about {340} m/s. · Sound is faster in water than in air, but faster still in a solid. · Sound cannot travel through a vacuum at all. | The closer the particles, the faster the vibration is passed on: solids, then liquids, then gases. |
| Why does sound travel faster in water than in air? | The particles of water are much closer together, so the vibration is passed on more quickly | Water is colder than air · Water is a transverse medium · Sound is louder under water | Temperature changes the speed a little, but the spacing of the particles matters far more. · Sound is longitudinal in water as it is in air. · How loud a sound is does not change how fast it travels. | Sound travels at about {340} m/s in air and about {1500} m/s in water. |
| A thunderclap is heard several seconds after the lightning is seen. Why? | Light travels far faster than sound, so the sound arrives much later | The thunder happens after the lightning · The sound is reflected by the clouds first · Sound slows down in damp air | The flash and the clap happen together; it is the travel times that differ. · The delay is there even for a direct path; the difference in speed causes it. · Damp air changes the speed only slightly, far too little to explain seconds of delay. | Light crosses a few kilometres almost at once, while sound takes about {3} s for each kilometre. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does sound travel faster in water than in air?

- ◻️ Sound is louder under water  
  _↳ feedback if chosen: How loud a sound is does not change how fast it travels._
- ◻️ Water is colder than air  
  _↳ feedback if chosen: Temperature changes the speed a little, but the spacing of the particles matters far more._
- ✅ The particles of water are much closer together, so the vibration is passed on more quickly
- ◻️ Water is a transverse medium  
  _↳ feedback if chosen: Sound is longitudinal in water as it is in air._

Full working after a second miss:

> Sound travels at about 340 m/s in air and about 1500 m/s in water.  
> So the answer is The particles of water are much closer together, so the vibration is passed on more quickly.  

> In which does sound travel fastest?

- ✅ In a steel bar
- ◻️ In air  
  _↳ feedback if chosen: Sound is slowest of these in air, about 340 m/s._
- ◻️ In a vacuum  
  _↳ feedback if chosen: Sound cannot travel through a vacuum at all._
- ◻️ In water  
  _↳ feedback if chosen: Sound is faster in water than in air, but faster still in a solid._

Full working after a second miss:

> The closer the particles, the faster the vibration is passed on: solids, then liquids, then gases.  
> So the answer is In a steel bar.  

> In which does sound travel fastest?

- ◻️ In water  
  _↳ feedback if chosen: Sound is faster in water than in air, but faster still in a solid._
- ✅ In a steel bar
- ◻️ In air  
  _↳ feedback if chosen: Sound is slowest of these in air, about 340 m/s._
- ◻️ In a vacuum  
  _↳ feedback if chosen: Sound cannot travel through a vacuum at all._

Full working after a second miss:

> The closer the particles, the faster the vibration is passed on: solids, then liquids, then gases.  
> So the answer is In a steel bar.  

Sources: sound (Form 4 Physics syllabus, Term 1: production and transmission of sound; characteristics of sound; measurement of the speed of sound by the echo and gun-firing methods; application of echo in sea bed depth)

### `p4-13-quality-card` · Lesson 13 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| The same note is played on a guitar and on a flute, equally loudly. Which statement is true? | They have the same pitch and loudness but different quality, because of their different overtones | They have different pitches · The flute sound travels faster · They are identical sounds | Playing 'the same note' means the same fundamental frequency, so the pitch is the same. · All sounds travel at the same speed in the same air. · They are easy to tell apart, which is why quality is a separate characteristic. | Each instrument adds its own mixture of overtones to the fundamental, and that mixture is its quality. |
| What makes one person's voice sound different from another's, even on the same note? | The mixture of overtones each voice produces, which is its quality | The speed of the sound each makes · The pitch of the note · The loudness of the voice | All voices travel at the same speed in the same air. · Singing the same note means the same pitch for both. · Both can sing equally loudly and still sound different. | Quality, or timbre, comes from the overtones present along with the fundamental. |
| A tuning fork and a violin both sound a note of {256} Hz. Why does the fork sound plainer? | A tuning fork gives almost only the fundamental, with few overtones | A tuning fork is quieter · A tuning fork gives a higher pitch · A tuning fork makes a longitudinal wave and the violin a transverse one | A fork can be struck hard and still sound plain. · Both sound {256} Hz, so the pitch is the same. · Both make longitudinal sound waves in the air. | A nearly pure note has little beyond the fundamental; the extra overtones of a violin give it a richer quality. |
| Which characteristic of a sound depends on the amplitude of the wave? | Its loudness | Its pitch · Its quality · Its speed | Pitch depends on the frequency. · Quality depends on the mixture of overtones. · The speed depends on the medium, not on the wave's amplitude. | A larger amplitude carries more energy, and the sound is louder. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What makes one person's voice sound different from another's, even on the same note?

- ✅ The mixture of overtones each voice produces, which is its quality
- ◻️ The loudness of the voice  
  _↳ feedback if chosen: Both can sing equally loudly and still sound different._
- ◻️ The speed of the sound each makes  
  _↳ feedback if chosen: All voices travel at the same speed in the same air._
- ◻️ The pitch of the note  
  _↳ feedback if chosen: Singing the same note means the same pitch for both._

Full working after a second miss:

> Quality, or timbre, comes from the overtones present along with the fundamental.  
> So the answer is The mixture of overtones each voice produces, which is its quality.  

> The same note is played on a guitar and on a flute, equally loudly. Which statement is true?

- ◻️ They have different pitches  
  _↳ feedback if chosen: Playing 'the same note' means the same fundamental frequency, so the pitch is the same._
- ◻️ They are identical sounds  
  _↳ feedback if chosen: They are easy to tell apart, which is why quality is a separate characteristic._
- ✅ They have the same pitch and loudness but different quality, because of their different overtones
- ◻️ The flute sound travels faster  
  _↳ feedback if chosen: All sounds travel at the same speed in the same air._

Full working after a second miss:

> Each instrument adds its own mixture of overtones to the fundamental, and that mixture is its quality.  
> So the answer is They have the same pitch and loudness but different quality, because of their different overtones.  

> What makes one person's voice sound different from another's, even on the same note?

- ◻️ The loudness of the voice  
  _↳ feedback if chosen: Both can sing equally loudly and still sound different._
- ◻️ The pitch of the note  
  _↳ feedback if chosen: Singing the same note means the same pitch for both._
- ✅ The mixture of overtones each voice produces, which is its quality
- ◻️ The speed of the sound each makes  
  _↳ feedback if chosen: All voices travel at the same speed in the same air._

Full working after a second miss:

> Quality, or timbre, comes from the overtones present along with the fundamental.  
> So the answer is The mixture of overtones each voice produces, which is its quality.  

Sources: sound (Form 4 Physics syllabus, Term 1: production and transmission of sound; characteristics of sound; measurement of the speed of sound by the echo and gun-firing methods; application of echo in sea bed depth)

