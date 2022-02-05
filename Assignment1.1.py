MalesStr=input('Number of Males:')
FemalesStr=input('Number of Females:')
Males=int(MalesStr)
Females=int(FemalesStr)
TotalInClass=Males+Females
print('Total In Class:', TotalInClass)
MalePercentage=(Males/TotalInClass)*100
print('Male Percentage:%.2f'% MalePercentage)
FemalePercentage=(Females/TotalInClass)*100
print('Female Percentage: %.2f'% FemalePercentage)