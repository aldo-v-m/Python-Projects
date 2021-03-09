%Assignment 2 - Data Preprocessing

table = readtable("Table_Assignment2.csv","EmptyValue",0,"ReadVariableNames",true);
table_array = table2array(table);

time = table_array(:,1);
temp = table_array(:,2);
calcium = table_array(:,3);

calcium_mean = calcium;
calcium_mean(10) = 5.1; %mean value
calcium_mean(13) = 5.1; %mean value

figure("Name", "Missing values with Mean Value")
plot(time, calcium_mean, "Marker","diamond","Color","r","LineWidth",2)
title("a) Missing Values with mean value (5.1)")
xlabel("Time")
ylabel("Calcium Cabonate")
grid on

calcium_neighbor = calcium;
calcium_neighbor(10) = mean([calcium_neighbor(9) calcium_neighbor(11)]); 
calcium_neighbor(13) = mean([calcium_neighbor(12) calcium_neighbor(14)]);

figure("Name", "Missing values with Neighboor mean values")
plot(time, calcium_neighbor, "Marker","o","Color","k","LineWidth",2)
title("b) Missing Values with Neighboor mean values")
xlabel("Time")
ylabel("Calcium Cabonate")
grid on


calcium_corr = calcium;
calcium_corr(10) = 1849.7*exp(-0.0063*temp(10));
calcium_corr(13) = 1849.7*exp(-0.0063*temp(13));

figure ("Name", "Correlation between temp and CaCO3")
plot(time, calcium_corr, "Marker","+","Color","b","LineWidth",2)
xlabel("Time")
ylabel("Calcium Cabonate")
title("c) Missing Values with correlation formula (temp-CaCO3)")
grid on