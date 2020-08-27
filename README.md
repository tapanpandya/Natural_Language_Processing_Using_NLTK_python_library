## Text data

Student	Engineer	Engineer
Engineer	Student 
	Student
Student		Student

# Term Frequency(TF) = number of each word present in a sentence divide by total number of words in a sentence.

# TF = Number of occurences for a word in a sentence / total number of words in a sentence.

	Sentence 1  Sentence 2  Sentence 3  Sentence 4
Student	  1/3		1/2	   1/1		2/2
Engineer  2/3		1/2	   0		0

# Inverse Document Frequency(IDF) = number sentences/number of sentences containing word

Words	  IDF(Occurences)
Student     Log(4/5)
Engineer    Log(4/3)

Finally, in order to calculate the final features importances,
We need to multiply values of TF table and IDF

So,	Student Engineer
	    Feature 1       	Feature 2 
S1  (1/3)*Log(4/5)    (2/3)*Log(4/3)
S2  (1/2)*Log(4/5)    (1/2)*Log(4/3)
S3  (1/1)*Log(4/5)    (0)*Log(4/3)
S4  (2/2)*Log(4/5)    (0)*Log(4/3)
