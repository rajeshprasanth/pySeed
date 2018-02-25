#!/usr/bin/env python

data_x, data_y = [],[]

def readcards(filename):
	file = open(filename,'r')
	for line in file:
		if not line.startswith("#"):
			if "SampleName" in line:
				SampleName = line.strip().split(":")[1]
			elif "FileFormat" in line:
				FileFormat = line.strip().split(":")[1]
			elif "TotalNumSeeds" in line:
				TotalNumSeeds = float(line.strip().split(":")[1])
			elif "CurveFitModel" in line:
				CurveFitModel = line.strip().split(":")[1]
			elif "IndependentVariable" in line:
				IndependentVariable = line.strip().split(":")[1]
			elif "DependentVariable" in line:
				DependentVariable = line.strip().split(":")[1]	
	return SampleName, FileFormat, TotalNumSeeds, CurveFitModel, IndependentVariable, DependentVariable

def readdata(filename):
	file = open(filename,'r')
	for line in file:
		if line.strip() == 'StartData' in line:
			break
	for line in file:
		if line.strip() == 'EndData' in line:
			break
		data_x.append(float(line.split()[0]))
		data_y.append(float(line.split()[1]))
		
	return data_x,data_y
	
def readinputfile(filename):
	SampleName, FileFormat, TotalNumSeeds, CurveFitModel, IndependentVariable, DependentVariable = readcards(filename)
	data_x,data_y = readdata(filename)
	return SampleName, FileFormat, TotalNumSeeds, CurveFitModel, IndependentVariable, DependentVariable, data_x, data_y

def checkconsistency(filename):
	SampleName, FileFormat, TotalNumSeeds, CurveFitModel, IndependentVariable, DependentVariable,data_x,data_y = readinputfile(filename)
	
	if (SampleName.strip() == ""):
		SampleName = "PySeed"
	
	if (FileFormat == "raw"):
		if ((TotalNumSeeds) <= 0 ):
			print "Incorrect Card in",filename,":: TotalNumSeeds should be > 0"
		else:
			data_y_temp = (data_y/TotalNumSeeds)*100
		exit()
	print SampleName, FileFormat, TotalNumSeeds, CurveFitModel, IndependentVariable, DependentVariable,data_x,data_y
checkconsistency('test1.dat')
