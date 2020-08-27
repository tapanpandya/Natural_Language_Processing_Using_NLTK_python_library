import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
from sklearn.feature_extraction.text import CountVectorizer
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

data = """  Workplace software company Okta said Thursday it plans to let most of its employees work remotely on a permanent basis, becoming the latest Silicon Valley company to adopt sweeping office policy changes amid the pandemic — and in the face of shifting US immigration policy.
Okta, which provides worker-login software to nearly 9,000 organizations including JetBlue, Nordstrom and Slack, said as much as 85% of its workforce is expected to work remotely under the new policy, up from 30% before the coronavirus crisis. The company has roughly 2,600 employees.
The decision highlights how US businesses are increasingly bracing for a long pandemic. Google has extended its remote work policies until at least July 2021. Earlier this week, Airbnb said it will allow its employees to work remotely through next August, even if their local offices have reopened.
Okta's move shows how a workplace trend toward permanently supporting work-from-anywhere, which began during the pandemic with Twitter and Facebook, is accelerating.
This spring, Okta told employees they could choose not to return to the office until a vaccine or effective treatment to Covid-19 has been developed. The announcement reflected partial steps toward a plan for remote work that Okta had started discussing the year before, said Todd McKinnon, Okta's CEO, in an interview. But the pandemic's enduring effects, along with recent US immigration restrictions announced by President Donald Trump, have sped up those plans.
"We're very fortunate in that the whole premise of our product is 'boundary-less work environments,'" McKinnon said.
About 70 Okta employees have already sought to take advantage of the remote work policy. Among them are a handful of employees outside the United States who could not enter the country to work due to Trump's extended limits on temporary worker visas, which were announced in June and strongly opposed by the tech industry.
Another group of foreign-born employees asked to work remotely full-time because they feared the uncertainty created by the administration's policies, according to McKinnon, who described himself as "frustrated" by the rules.
"Directly because of what the US administration is doing, it's led them to not want to have to deal with the problem and we've been able to move them to other countries, like Canada," McKinnon said. "Maybe their visa is coming up in a year, or they're concerned about the green card process, so they're moving to a different country. But it's a shame for the US."
Other factors encouraging Okta to shift to permanent remote work included workers' growing comfort with technology and economic trends such as the high costs of living in New York and San Francisco, according to an internal presentation reviewed by CNN.
Okta's internal surveys showed strong demand for more work-from-anywhere flexibility. Roughly eight in 10 employees said they would feel as or more productive working remotely than in the office, according to data the company collected in 2019. Just 17% said they would prefer to work five days a week inside an office.
The new plan could also mean changes in worker pay. Like Facebook, which has signaled it will change compensation for those choosing to work outside major tech hubs, Okta said employees who wish to work remotely will undergo a similar approval process.
That process will account for local costs of living, how long an employee has worked at the company and an area's comparable benefits and salaries.
Still, said McKinnon, as more companies shift to permanent remote work, the less local geography will play a role in compensation and the more pay will again be defined by a worker's qualifications.
"You'll see more consistent salaries around the world," McKinnon said. "Facebook is going to hire an engineer in Raleigh, just like we will. The determinant will not be what the cost of living in Raleigh is, but what Facebook or Okta will pay."
"""

## Lemmatization technique
# Creates the separate sentences out of entire data.
sentences = nltk.sent_tokenize(data)

# Extracts main points from the text data but meaning might be changed due to removal of suffix or prefix
# to make base of each word. i.e. cleaning would be converted to clean after applying stemming.
lemmatizer = WordNetLemmatizer()
corpus = []

## Stemmer technique
for i in range(len(sentences)):
    words = re.sub('[^a-zA-Z]', ' ', sentences[i])
    words = words.lower()
    words = words.split()
                            # # Separates the words from each sentences.
                            # words = nltk.word_tokenize(sentences[i])
    # Applying stemming on each words after removing words
    # which does not add values to the data by using stopwords() which is available in various languages.
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    words = ' '.join(words)
    corpus.append(words)

print('result after lemmatization technique on text data')
for i in range(len(corpus)):
    print(corpus[i])

## Now coming to Bag of Words

# It is a technique to count the number of occurances of a word in each sentence.
# so, for each word the word would have a number through which machine learning model determine the importance of
# a particular word.

# Not recommended for huge dataset and it only give you number of occurances which is not sufficient to come to conclusion.

cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()

print(X)
