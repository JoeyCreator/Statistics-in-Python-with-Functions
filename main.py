import statistics
 
numbers = [100.1, 300.3, 300.3, 400.4, 500.5, 700.7]
  
mean = statistics.mean(numbers)
print('Mean of data: ', mean)
 
harmonic_mean = statistics.harmonic_mean(numbers)
print('Harmonic mean of data: ', harmonic_mean)
 
median = statistics.median(numbers)
print('Median of data : ', median)
 
median_low = statistics.median_low(numbers)
print('Low median of data: ', median_low)
 
median_high = statistics.median_high(numbers)
print('High median of data: ', median_high)
 
median_grouped = statistics.median_grouped(numbers)
print('Median, or 50th percentile, of grouped data: ', median_grouped)
 
mode = statistics.mode(numbers)
print('Mode (most common value) of discrete data: ', mode)