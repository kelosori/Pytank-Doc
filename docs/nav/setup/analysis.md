# **Analyzing with Pytank**

Pytank main objective is to estimate the original oil in place (OOIP), using
the material balance as the main tool. That is why two important concepts have
to be taken into account, which are the **subsurface withdrawal** and the
**average pressure**.

The calculation of average pressures and subway withdrawal are key concepts in
reservoir engineering, especially when performing a material balance analysis
and determining the behavior of a reservoir in terms of production and reserves.
Below is a description of each, their relationship and their importance in the
context of a reservoir's POES (Production, Operation, Efficiency and
Sustainability) analysis.

## **Average Pressure**

The average pressure in a reservoir refers to the average pressure found in the
reservoir during a given period. This calculation is made from pressure
measurements taken at different times and locations within the reservoir. The
average pressure is crucial to understanding how reservoir conditions vary as
fluids are withdrawn.

## **Underground Withdrawal**

Underground withdrawal refers to the amount of fluids (oil, gas and water) that
are extracted from the reservoir through the wells. This calculation considers
cumulative production and is used to evaluate the efficiency of resource
extraction in the reservoir. Subsurface withdrawal is essential to determine how
fluid withdrawal affects pressure and saturation in the reservoir.

Average pressure and drawdown are interrelated in the analysis of reservoir
behavior. As subsurface drawdown occurs, the pressure in the reservoir tends to
decrease. This, in turn, can affect the reservoir's ability to continue
producing fluids efficiently. Therefore, a proper analysis of both parameters is
critical to understanding the state of the reservoir and predicting its future
behavior.

## **Importance in OOIP Analysis**

OOIP analysis focuses on the production, operation, efficiency and
sustainability of a reservoir. Average pressure and subsurface withdrawal are
critical components in this analysis for several reasons:

- **Reservoir Evaluation**: Knowing the average pressure allows engineers to
  estimate the original volume of oil and gas in the reservoir. This is
  fundamental to production planning and reservoir management.
- **Production Optimization**: Monitoring subsurface withdrawal helps engineers
  adjust production strategies. If the subway withdrawal is too high and the
  average pressure is decreasing rapidly, it may be necessary to change the
  extraction technique or implement enhanced recovery methods.
- **Predicting Reservoir Behavior**: By analyzing the relationship between
  average
  pressure and drawdown, engineers can predict how the reservoir will respond to
  different production scenarios. This is essential for making informed
  decisions about field operation.
- **Sustainability**: Proper management of subsurface pressure and drawdown is
  key to reservoir sustainability. Maintaining pressure at optimal levels helps
  extend reservoir life and maximize resource recovery.

## **Campbell Method**

The Campbell method is used in reservoir engineering to analyze the energy
contribution of an aquifer in relation to oil production. This method allows the
relationship between cumulative oil production (Np) and aquifer energy (F/Eo +
Efw) to be graphed, making it easier to visualize how the aquifer affects
reservoir production.

The importance of the Campbell method lies in its ability to provide a graphical
representation of the influence of the aquifer on oil production. By performing
a material balance analysis, engineers can determine how aquifer energy
contributes to oil recovery. This is essential for:

- **Optimizing production**: Understanding the relationship between production
  and aquifer energy allows engineers to adjust production strategies to
  maximize hydrocarbon recovery.
- **Evaluating reserves**: The method helps estimate the volume of oil that can
  be recovered, which is crucial for production planning and reserve evaluation.

## **Havlena-Odeh method**

The Havlena-Odeh method is a technique used to analyse oil production in fields
that are influenced by aquifers. This method is based on the relationship
between aquifer energy and cumulative oil production, allowing the calculation
of pressure and expected production based on historical data.

The Havlena-Odeh method is essential in material balance analysis for the
following reasons:

- **Calculation of OOIP**: This method allows the calculation of the inferred
  OOIP (Original-Oil-in-Place), which is essential for assessing the amount of
  oil that can be recovered from a field. Accuracy in the estimation of POES is
  vital for planning and decision-making in the exploitation of the field.
- **Comparison of pressures**: The method allows the comparison of observed
  pressure with calculated pressure, helping to identify discrepancies that may
  indicate problems in the field or in the modelling of the aquifer.
- **Aquifer modeling**: By incorporating aquifer models such as Fetkovich and
  Carter-Tracy, the method provides a robust framework for understanding how the
  aquifer affects oil production, which is crucial for effective resource
  management.

## **Analysis Class**

The Analysis class includes a private method called `_pressure_vol_avg`, which
is responsible for calculating the average pressure in the reservoir. This
method uses underground pressure and withdrawal data to determine the average
pressure over time. Average pressure is crucial to understanding how fluid
extraction affects reservoir conditions and to predict future reservoir
behavior.

The class also includes a private method called `_calc_uw`, which calculates
underground withdrawal per well. This method combines production and pressure
data to determine how much fluid has been removed from the reservoir.
Underground removal is essential to assess production efficiency and how it
affects pressure in the reservoir.

Pytank allows you to use two important graphical methods in the process so that
you can perform the respective analysis of your data: `Campbell` and
`Havlena & Odeh`.

### **Campbell Method**

The campbell_plot function generates a Campbell chart that illustrates the
relationship between cumulative oil output (Np) and aquifer energy (F/Eo + Efw).
This visualization is essential to understanding how the energy of the aquifer
contributes to oil recovery.

### **Havlena and Odeh Method**

This graph allows you to calculate the OOIP (Original Oil in Place). There are
two options to create the chart:

- Using the Campbell method, the presence of an aquifer can be inferred,
  indicating that a non-volumetric sub-saturated layer is being worked.
- In the absence of an energy supply, it is considered a volumetric
  sub-saturated
  reservoir.

### **Analytical Method**

This method is based on an inferred OOIP, which is used to recalculate a
synthetic pressure. The inferred POES is relevant when the pressure observed in
the reservoir shows a behavior similar to the calculated synthetic pressure. In
this case, it can be confirmed that the POES is suitable for the matter balance
equation.

For more information on the Analysis class you can review its
[documentation](/nav/API/analysis_api/).
