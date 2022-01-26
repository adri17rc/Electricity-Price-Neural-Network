# Electricity-Price-Neural-Network
NN for predictions of electricity prices in Spain's wholesale market based on gas and CO2 prices

Last year the whole world has experience a rise in energy prices, mostly driven by gas prices. This energy source is becoming more relevant as the world's leading countries are aiming for a decarbonization of the economy, and transition energies are claiming their market share to the detriment of the most polluting ones (i.e. coal and petrol). Hence, they have seen their demand continously increased, unlike the offer. Thus, and combined with geopolitical inestabilities we are not analyzing in this work, electricity prices have broken all the previous records throughout last 2021. 

The motivation behind the developed neural network is to predict the fluctuations in the electricity prices within the Iberian market (Spain and Portugal), based on previous data of gas and CO2 prices. We believe a proper prediction could help electro-intensive industries, and even home consumers, to plan electricity-demanding tasks, in order to minimize the impact on the electricity bill. The following graphs shows both the gas and MWh prices throughout last year. 

![EvolutionGasPrices2021](https://user-images.githubusercontent.com/96789733/151145957-9f4efd74-2f6d-4377-af62-c0324fe9f6ce.png)  ![EvolutionMWhPrices2021](https://user-images.githubusercontent.com/96789733/151146102-1df39c2c-a23f-4077-a059-cc0f278b770c.png)

Graphs confirm the rise in prices, mostly in the second half of the year. Correlation between gas and electricity prices can be confirmed by a more detailed study of the electricity pricing system. Basically, the most expensive source of energy is the one that sets the final price. In 2020, combined cycles set the price on 20.7% of the hours, whereas hidroelectic did it on 45.8% of the hours and renewable source on the 29.8% (Source:https://www.omie.es/sites/default/files/2021-01/informe_anual_2020_es.pdf). It may look hidroelectic production is responsible of the increase, but a closer look tell us hidroelectric prices are set taking gas-produced energy as a reference (source:https://www.businessinsider.es/como-fija-precio-luz-espana-790815).

##First Neural Network

The previous infromation justifies the development of a neural network able to find the relation between both variables and predict the future behaviour of the market. Python was chosen to program the model, together with the following libraries: Numpy, Tensorflow, Keras and Matplotlib. The neural network consisted in 3 fully-connected hidden layers model, with 12, 8 and 4 nodes repectively, yielding 181 trainable parameters. More complex structures were trained, showing no noticeable improvement in results. 



##Second Neural Network



