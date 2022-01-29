# Electricity-Price-Neural-Network
NN for predictions of electricity prices in Spain's wholesale market based on gas and CO2 prices

Last year the whole world has experience a rise in energy prices, mostly driven by gas prices. This energy source is becoming more relevant as the world's leading countries are aiming for a decarbonization of the economy, and transition energies are claiming their market share to the detriment of the most polluting ones (i.e. coal and petrol). Hence, they have seen their demand continously increased, unlike the offer. Thus, and combined with geopolitical inestabilities we are not analyzing in this work, electricity prices have broken all the previous records throughout last 2021. 

The motivation behind the developed neural network is to predict the fluctuations in the electricity prices within the Iberian market (Spain and Portugal), based on previous data of gas and CO2 prices. We believe a proper prediction could help electro-intensive industries, and even home consumers, to plan electricity-demanding tasks, in order to minimize the impact on the electricity bill. The following graphs shows both the gas and MWh prices throughout last year. 

![EvolutionGasPrices2021](https://user-images.githubusercontent.com/96789733/151145957-9f4efd74-2f6d-4377-af62-c0324fe9f6ce.png)  ![EvolutionMWhPrices2021](https://user-images.githubusercontent.com/96789733/151146102-1df39c2c-a23f-4077-a059-cc0f278b770c.png)

Graphs confirm the rise in prices, mostly in the second half of the year. Correlation between gas and electricity prices can be confirmed by a more detailed study of the electricity pricing system. Basically, the most expensive source of energy is the one that sets the final price. In 2020, combined cycles set the price on 20.7% of the hours, whereas hidroelectic did it on 45.8% of the hours and renewable source on the 29.8% (Source:https://www.omie.es/sites/default/files/2021-01/informe_anual_2020_es.pdf). It may look hidroelectic production is responsible of the increase, but a closer look tell us hidroelectric prices are set taking gas-produced energy as a reference (source:https://www.businessinsider.es/como-fija-precio-luz-espana-790815).

##First Neural Network

The previous infromation justifies the development of a neural network able to find the relation between both variables and predict the future behaviour of the market. 
Python was chosen to program the model, together with the following libraries: Numpy, Tensorflow, Keras and Matplotlib. The neural network consists in 3 sequential fully-connected hidden layers model, with 12, 8 and 4 nodes repectively, yielding 181 trainable parameters. More complex structures were trained, showing no noticeable improvement in results. An EarlyStopping calback was added, to prevent overfitting of data (a common on problem on small datasets as the one used). To compile the model, the loss chosen was 'mean square error' and the optimizer 'rmsprop'; model yields no accuracy, since it is a regression problem, not a classification. Our 'x', or independet variable, were the gas prices from the 1/4/2021 to the 12/7/2021, whereas the 'y' or dependent variable were the electricity prices from the 1/11/2021 until 12/14/2021; that means a week shift between both variables, so that the model may have a predicitive usefulness.Once the model was trained, a prediction for the last 200 days of the train dataset was made (see plot below). In order to get an idea of how well the model may predict the future behaviour, the mean relative error was computed. 

###Results
The model was trained through 300 epochs with a batch size of 100. It showed good results on prediction, with an average mean relative error between 21-22%. The main deviations come from the extremely peak data on isolated days. This may respond to unusual demand or weather conditions on real life, which are extremely hard to predict within the logic of this model, since they don't obey variations on the gas market.
The test loss approached the train loss, proving the predictive character of the model. 

![Model_Loss_1](https://user-images.githubusercontent.com/96789733/151657402-87980037-7819-40cc-b7b6-c80f48047069.png) ![Prediction1_NN](https://user-images.githubusercontent.com/96789733/151657562-d3aff479-514e-4b53-aaf5-4244dd4a003b.png)



##Second Neural Network
A further study on the energy production gives another variable, strictly related with the consumption of gas: the CO2 (Carbon Dioxide) allowance emission cost, that is, the price that has to be paid to produce a ton of CO2. This is regulated by the RDCE UE, the common market to sell and purchase CO2 emission rights. The higher the cost of the allowance, the higher the cost of producing electricity in a combined cycle power plant. If we check the prices in 2021, a upward trend can be observed. 



