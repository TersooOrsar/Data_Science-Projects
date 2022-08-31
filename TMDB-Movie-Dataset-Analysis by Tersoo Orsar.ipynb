{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# TMDB Movie Dataset Analysis\n",
    "**Reported by Tersoo Orsar\n",
    "\n",
    "## Table of Contents\n",
    "<ul>\n",
    "<li><a href=\"#intro\">Introduction</a></li>\n",
    "<li><a href=\"#wrangling\">Data Wrangling</a></li>\n",
    "<li><a href=\"#eda\">Exploratory Data Analysis</a></li>\n",
    "<li><a href=\"#conclusions\">Conclusions</a></li>\n",
    "</ul>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# <a id='intro'></a>\n",
    "## Introduction\n",
    "\n",
    "### Dataset Description \n",
    "The dataset that will be analyzed in this report is the TMDB movie data containing information about 10,000 movies from The Movie Database (TMDB). The information includes some basic information about the movie like the title, cast, and director, and other relevant statistics such as popularity, budget, and revenue. In this report, the data analysis process will be used to answer the following questions:\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "### Question(s) for Analysis\n",
    "**1.What kinds of properties are associated with movies that have high revenues?\n",
    "\n",
    "**2.Which genres are most popular from year to year?. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This report will use some libaries of Python including Numpy, Pandas, and Matplotlib. The import statement of these libraries is stated below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#loading necessary libraries\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='wrangling'></a>\n",
    "## Data Wrangling\n",
    "\n",
    "Reading the Data:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load your data\n",
    "\n",
    "movie_data = pd.read_csv('tmdb-movies.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10866, 21)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Find out the number rows and columns in the dataset\n",
    "movie_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['id', 'imdb_id', 'popularity', 'budget', 'revenue',\n",
       "       'original_title', 'cast', 'homepage', 'director', 'tagline',\n",
       "       'keywords', 'overview', 'runtime', 'genres', 'production_companies',\n",
       "       'release_date', 'vote_count', 'vote_average', 'release_year',\n",
       "       'budget_adj', 'revenue_adj'], dtype=object)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Find out the names of the columns in the dataset\n",
    "movie_data.columns.values"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Inspecting the 5 first rows from the Data\n",
    "Here it is presented the first 5 rows from the TMdb dataset, Lets look at each column. \n",
    "There are id columns as a unique value corresponding to each row - entry, which on its side represents each movie. \n",
    "There are other columns which describes financial values such budget and revenue. \n",
    "Other columns include information like the genre of this movie, the production companies, the release_date, the crowd's votes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>homepage</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>...</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>budget_adj</th>\n",
       "      <th>revenue_adj</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>135397</td>\n",
       "      <td>tt0369610</td>\n",
       "      <td>32.985763</td>\n",
       "      <td>150000000</td>\n",
       "      <td>1513528810</td>\n",
       "      <td>Jurassic World</td>\n",
       "      <td>Chris Pratt|Bryce Dallas Howard|Irrfan Khan|Vi...</td>\n",
       "      <td>http://www.jurassicworld.com/</td>\n",
       "      <td>Colin Trevorrow</td>\n",
       "      <td>The park is open.</td>\n",
       "      <td>...</td>\n",
       "      <td>Twenty-two years after the events of Jurassic ...</td>\n",
       "      <td>124</td>\n",
       "      <td>Action|Adventure|Science Fiction|Thriller</td>\n",
       "      <td>Universal Studios|Amblin Entertainment|Legenda...</td>\n",
       "      <td>6/9/15</td>\n",
       "      <td>5562</td>\n",
       "      <td>6.5</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.379999e+08</td>\n",
       "      <td>1.392446e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>76341</td>\n",
       "      <td>tt1392190</td>\n",
       "      <td>28.419936</td>\n",
       "      <td>150000000</td>\n",
       "      <td>378436354</td>\n",
       "      <td>Mad Max: Fury Road</td>\n",
       "      <td>Tom Hardy|Charlize Theron|Hugh Keays-Byrne|Nic...</td>\n",
       "      <td>http://www.madmaxmovie.com/</td>\n",
       "      <td>George Miller</td>\n",
       "      <td>What a Lovely Day.</td>\n",
       "      <td>...</td>\n",
       "      <td>An apocalyptic story set in the furthest reach...</td>\n",
       "      <td>120</td>\n",
       "      <td>Action|Adventure|Science Fiction|Thriller</td>\n",
       "      <td>Village Roadshow Pictures|Kennedy Miller Produ...</td>\n",
       "      <td>5/13/15</td>\n",
       "      <td>6185</td>\n",
       "      <td>7.1</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.379999e+08</td>\n",
       "      <td>3.481613e+08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>262500</td>\n",
       "      <td>tt2908446</td>\n",
       "      <td>13.112507</td>\n",
       "      <td>110000000</td>\n",
       "      <td>295238201</td>\n",
       "      <td>Insurgent</td>\n",
       "      <td>Shailene Woodley|Theo James|Kate Winslet|Ansel...</td>\n",
       "      <td>http://www.thedivergentseries.movie/#insurgent</td>\n",
       "      <td>Robert Schwentke</td>\n",
       "      <td>One Choice Can Destroy You</td>\n",
       "      <td>...</td>\n",
       "      <td>Beatrice Prior must confront her inner demons ...</td>\n",
       "      <td>119</td>\n",
       "      <td>Adventure|Science Fiction|Thriller</td>\n",
       "      <td>Summit Entertainment|Mandeville Films|Red Wago...</td>\n",
       "      <td>3/18/15</td>\n",
       "      <td>2480</td>\n",
       "      <td>6.3</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.012000e+08</td>\n",
       "      <td>2.716190e+08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>140607</td>\n",
       "      <td>tt2488496</td>\n",
       "      <td>11.173104</td>\n",
       "      <td>200000000</td>\n",
       "      <td>2068178225</td>\n",
       "      <td>Star Wars: The Force Awakens</td>\n",
       "      <td>Harrison Ford|Mark Hamill|Carrie Fisher|Adam D...</td>\n",
       "      <td>http://www.starwars.com/films/star-wars-episod...</td>\n",
       "      <td>J.J. Abrams</td>\n",
       "      <td>Every generation has a story.</td>\n",
       "      <td>...</td>\n",
       "      <td>Thirty years after defeating the Galactic Empi...</td>\n",
       "      <td>136</td>\n",
       "      <td>Action|Adventure|Science Fiction|Fantasy</td>\n",
       "      <td>Lucasfilm|Truenorth Productions|Bad Robot</td>\n",
       "      <td>12/15/15</td>\n",
       "      <td>5292</td>\n",
       "      <td>7.5</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.839999e+08</td>\n",
       "      <td>1.902723e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>168259</td>\n",
       "      <td>tt2820852</td>\n",
       "      <td>9.335014</td>\n",
       "      <td>190000000</td>\n",
       "      <td>1506249360</td>\n",
       "      <td>Furious 7</td>\n",
       "      <td>Vin Diesel|Paul Walker|Jason Statham|Michelle ...</td>\n",
       "      <td>http://www.furious7.com/</td>\n",
       "      <td>James Wan</td>\n",
       "      <td>Vengeance Hits Home</td>\n",
       "      <td>...</td>\n",
       "      <td>Deckard Shaw seeks revenge against Dominic Tor...</td>\n",
       "      <td>137</td>\n",
       "      <td>Action|Crime|Thriller</td>\n",
       "      <td>Universal Pictures|Original Film|Media Rights ...</td>\n",
       "      <td>4/1/15</td>\n",
       "      <td>2947</td>\n",
       "      <td>7.3</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.747999e+08</td>\n",
       "      <td>1.385749e+09</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       id    imdb_id  popularity     budget     revenue  \\\n",
       "0  135397  tt0369610   32.985763  150000000  1513528810   \n",
       "1   76341  tt1392190   28.419936  150000000   378436354   \n",
       "2  262500  tt2908446   13.112507  110000000   295238201   \n",
       "3  140607  tt2488496   11.173104  200000000  2068178225   \n",
       "4  168259  tt2820852    9.335014  190000000  1506249360   \n",
       "\n",
       "                 original_title  \\\n",
       "0                Jurassic World   \n",
       "1            Mad Max: Fury Road   \n",
       "2                     Insurgent   \n",
       "3  Star Wars: The Force Awakens   \n",
       "4                     Furious 7   \n",
       "\n",
       "                                                cast  \\\n",
       "0  Chris Pratt|Bryce Dallas Howard|Irrfan Khan|Vi...   \n",
       "1  Tom Hardy|Charlize Theron|Hugh Keays-Byrne|Nic...   \n",
       "2  Shailene Woodley|Theo James|Kate Winslet|Ansel...   \n",
       "3  Harrison Ford|Mark Hamill|Carrie Fisher|Adam D...   \n",
       "4  Vin Diesel|Paul Walker|Jason Statham|Michelle ...   \n",
       "\n",
       "                                            homepage          director  \\\n",
       "0                      http://www.jurassicworld.com/   Colin Trevorrow   \n",
       "1                        http://www.madmaxmovie.com/     George Miller   \n",
       "2     http://www.thedivergentseries.movie/#insurgent  Robert Schwentke   \n",
       "3  http://www.starwars.com/films/star-wars-episod...       J.J. Abrams   \n",
       "4                           http://www.furious7.com/         James Wan   \n",
       "\n",
       "                         tagline      ...       \\\n",
       "0              The park is open.      ...        \n",
       "1             What a Lovely Day.      ...        \n",
       "2     One Choice Can Destroy You      ...        \n",
       "3  Every generation has a story.      ...        \n",
       "4            Vengeance Hits Home      ...        \n",
       "\n",
       "                                            overview runtime  \\\n",
       "0  Twenty-two years after the events of Jurassic ...     124   \n",
       "1  An apocalyptic story set in the furthest reach...     120   \n",
       "2  Beatrice Prior must confront her inner demons ...     119   \n",
       "3  Thirty years after defeating the Galactic Empi...     136   \n",
       "4  Deckard Shaw seeks revenge against Dominic Tor...     137   \n",
       "\n",
       "                                      genres  \\\n",
       "0  Action|Adventure|Science Fiction|Thriller   \n",
       "1  Action|Adventure|Science Fiction|Thriller   \n",
       "2         Adventure|Science Fiction|Thriller   \n",
       "3   Action|Adventure|Science Fiction|Fantasy   \n",
       "4                      Action|Crime|Thriller   \n",
       "\n",
       "                                production_companies release_date vote_count  \\\n",
       "0  Universal Studios|Amblin Entertainment|Legenda...       6/9/15       5562   \n",
       "1  Village Roadshow Pictures|Kennedy Miller Produ...      5/13/15       6185   \n",
       "2  Summit Entertainment|Mandeville Films|Red Wago...      3/18/15       2480   \n",
       "3          Lucasfilm|Truenorth Productions|Bad Robot     12/15/15       5292   \n",
       "4  Universal Pictures|Original Film|Media Rights ...       4/1/15       2947   \n",
       "\n",
       "   vote_average  release_year    budget_adj   revenue_adj  \n",
       "0           6.5          2015  1.379999e+08  1.392446e+09  \n",
       "1           7.1          2015  1.379999e+08  3.481613e+08  \n",
       "2           6.3          2015  1.012000e+08  2.716190e+08  \n",
       "3           7.5          2015  1.839999e+08  1.902723e+09  \n",
       "4           7.3          2015  1.747999e+08  1.385749e+09  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 10866 entries, 0 to 10865\n",
      "Data columns (total 21 columns):\n",
      "id                      10866 non-null int64\n",
      "imdb_id                 10856 non-null object\n",
      "popularity              10866 non-null float64\n",
      "budget                  10866 non-null int64\n",
      "revenue                 10866 non-null int64\n",
      "original_title          10866 non-null object\n",
      "cast                    10790 non-null object\n",
      "homepage                2936 non-null object\n",
      "director                10822 non-null object\n",
      "tagline                 8042 non-null object\n",
      "keywords                9373 non-null object\n",
      "overview                10862 non-null object\n",
      "runtime                 10866 non-null int64\n",
      "genres                  10843 non-null object\n",
      "production_companies    9836 non-null object\n",
      "release_date            10866 non-null object\n",
      "vote_count              10866 non-null int64\n",
      "vote_average            10866 non-null float64\n",
      "release_year            10866 non-null int64\n",
      "budget_adj              10866 non-null float64\n",
      "revenue_adj             10866 non-null float64\n",
      "dtypes: float64(4), int64(6), object(11)\n",
      "memory usage: 1.7+ MB\n"
     ]
    }
   ],
   "source": [
    "#Assessing the data to know its structure.\n",
    "movie_data.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Cleaning: Clean the duplicated row and NaN values\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Firstly, we need to check if there are any duplicated rows in this data set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check the duplicated row\n",
    "movie_data.duplicated().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There is one duplicated row in the dataset, so this row will be dropped"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Drop the duplicated row and check if there are no duplicated rows after cleaning\n",
    "movie_data.drop_duplicates(inplace=True)\n",
    "movie_data.duplicated().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "Following, based on the research question above, it is obviously that not all columns are needed for analysis. Thus, the irrelevant columns are dropped and only relevant columns are kept for the further analysis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>budget_adj</th>\n",
       "      <th>revenue_adj</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>32.985763</td>\n",
       "      <td>150000000</td>\n",
       "      <td>1513528810</td>\n",
       "      <td>124</td>\n",
       "      <td>Action|Adventure|Science Fiction|Thriller</td>\n",
       "      <td>5562</td>\n",
       "      <td>6.5</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.379999e+08</td>\n",
       "      <td>1.392446e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>28.419936</td>\n",
       "      <td>150000000</td>\n",
       "      <td>378436354</td>\n",
       "      <td>120</td>\n",
       "      <td>Action|Adventure|Science Fiction|Thriller</td>\n",
       "      <td>6185</td>\n",
       "      <td>7.1</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.379999e+08</td>\n",
       "      <td>3.481613e+08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>13.112507</td>\n",
       "      <td>110000000</td>\n",
       "      <td>295238201</td>\n",
       "      <td>119</td>\n",
       "      <td>Adventure|Science Fiction|Thriller</td>\n",
       "      <td>2480</td>\n",
       "      <td>6.3</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.012000e+08</td>\n",
       "      <td>2.716190e+08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>11.173104</td>\n",
       "      <td>200000000</td>\n",
       "      <td>2068178225</td>\n",
       "      <td>136</td>\n",
       "      <td>Action|Adventure|Science Fiction|Fantasy</td>\n",
       "      <td>5292</td>\n",
       "      <td>7.5</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.839999e+08</td>\n",
       "      <td>1.902723e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>9.335014</td>\n",
       "      <td>190000000</td>\n",
       "      <td>1506249360</td>\n",
       "      <td>137</td>\n",
       "      <td>Action|Crime|Thriller</td>\n",
       "      <td>2947</td>\n",
       "      <td>7.3</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.747999e+08</td>\n",
       "      <td>1.385749e+09</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   popularity     budget     revenue  runtime  \\\n",
       "0   32.985763  150000000  1513528810      124   \n",
       "1   28.419936  150000000   378436354      120   \n",
       "2   13.112507  110000000   295238201      119   \n",
       "3   11.173104  200000000  2068178225      136   \n",
       "4    9.335014  190000000  1506249360      137   \n",
       "\n",
       "                                      genres  vote_count  vote_average  \\\n",
       "0  Action|Adventure|Science Fiction|Thriller        5562           6.5   \n",
       "1  Action|Adventure|Science Fiction|Thriller        6185           7.1   \n",
       "2         Adventure|Science Fiction|Thriller        2480           6.3   \n",
       "3   Action|Adventure|Science Fiction|Fantasy        5292           7.5   \n",
       "4                      Action|Crime|Thriller        2947           7.3   \n",
       "\n",
       "   release_year    budget_adj   revenue_adj  \n",
       "0          2015  1.379999e+08  1.392446e+09  \n",
       "1          2015  1.379999e+08  3.481613e+08  \n",
       "2          2015  1.012000e+08  2.716190e+08  \n",
       "3          2015  1.839999e+08  1.902723e+09  \n",
       "4          2015  1.747999e+08  1.385749e+09  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Drop the irrelevant columns\n",
    "drop_columns = ['id', 'imdb_id', 'original_title', 'cast', 'homepage',\n",
    "             'tagline', 'keywords', 'overview', 'release_date', 'director', 'production_companies']\n",
    "movie_data.drop(drop_columns, axis=1, inplace=True)\n",
    "movie_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "some data in \"genres\" are missed. In order to analyze the data, the row containing the null value will be dropped."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Drop the row with the NaN value and check if there are NaN values after dropping\n",
    "movie_data.dropna(inplace=True)\n",
    "movie_data.isnull().sum().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Exploratory Data Analysis\n",
    "Research Question 1: What kinds of properties are associated with movies that have high revenues?\n",
    "To answer this question, we need to define what the high revenue is. Firstly, we need to discover the property of the revenue."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    1.084200e+04\n",
       "mean     3.991138e+07\n",
       "std      1.171179e+08\n",
       "min      0.000000e+00\n",
       "25%      0.000000e+00\n",
       "50%      0.000000e+00\n",
       "75%      2.414118e+07\n",
       "max      2.781506e+09\n",
       "Name: revenue, dtype: float64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Discover the statistics of revenue\n",
    "movie_data.revenue.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The change of revenue over year and the distribution of revenue are shown below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fac0a4a25f8>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Draw the line char for the change of the revenue\n",
    "revenues = movie_data.groupby('release_year')['revenue'].mean()\n",
    "\n",
    "plt.plot(revenues)\n",
    "plt.title('The revenue change from year to year')\n",
    "plt.xlabel('Year')\n",
    "plt.ylabel('Revenue')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the line chart above, the revenue changed drastically over the year, especially during the period of 1960s. However, the revenue shows an increasing trend from the overall perspective. Next, we need to compare the revenue in different years. Since there are too many years, we aggregate them into decades"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>budget_adj</th>\n",
       "      <th>revenue_adj</th>\n",
       "      <th>decade</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>32.985763</td>\n",
       "      <td>150000000</td>\n",
       "      <td>1513528810</td>\n",
       "      <td>124</td>\n",
       "      <td>Action|Adventure|Science Fiction|Thriller</td>\n",
       "      <td>5562</td>\n",
       "      <td>6.5</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.379999e+08</td>\n",
       "      <td>1.392446e+09</td>\n",
       "      <td>2010s</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>28.419936</td>\n",
       "      <td>150000000</td>\n",
       "      <td>378436354</td>\n",
       "      <td>120</td>\n",
       "      <td>Action|Adventure|Science Fiction|Thriller</td>\n",
       "      <td>6185</td>\n",
       "      <td>7.1</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.379999e+08</td>\n",
       "      <td>3.481613e+08</td>\n",
       "      <td>2010s</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>13.112507</td>\n",
       "      <td>110000000</td>\n",
       "      <td>295238201</td>\n",
       "      <td>119</td>\n",
       "      <td>Adventure|Science Fiction|Thriller</td>\n",
       "      <td>2480</td>\n",
       "      <td>6.3</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.012000e+08</td>\n",
       "      <td>2.716190e+08</td>\n",
       "      <td>2010s</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>11.173104</td>\n",
       "      <td>200000000</td>\n",
       "      <td>2068178225</td>\n",
       "      <td>136</td>\n",
       "      <td>Action|Adventure|Science Fiction|Fantasy</td>\n",
       "      <td>5292</td>\n",
       "      <td>7.5</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.839999e+08</td>\n",
       "      <td>1.902723e+09</td>\n",
       "      <td>2010s</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>9.335014</td>\n",
       "      <td>190000000</td>\n",
       "      <td>1506249360</td>\n",
       "      <td>137</td>\n",
       "      <td>Action|Crime|Thriller</td>\n",
       "      <td>2947</td>\n",
       "      <td>7.3</td>\n",
       "      <td>2015</td>\n",
       "      <td>1.747999e+08</td>\n",
       "      <td>1.385749e+09</td>\n",
       "      <td>2010s</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   popularity     budget     revenue  runtime  \\\n",
       "0   32.985763  150000000  1513528810      124   \n",
       "1   28.419936  150000000   378436354      120   \n",
       "2   13.112507  110000000   295238201      119   \n",
       "3   11.173104  200000000  2068178225      136   \n",
       "4    9.335014  190000000  1506249360      137   \n",
       "\n",
       "                                      genres  vote_count  vote_average  \\\n",
       "0  Action|Adventure|Science Fiction|Thriller        5562           6.5   \n",
       "1  Action|Adventure|Science Fiction|Thriller        6185           7.1   \n",
       "2         Adventure|Science Fiction|Thriller        2480           6.3   \n",
       "3   Action|Adventure|Science Fiction|Fantasy        5292           7.5   \n",
       "4                      Action|Crime|Thriller        2947           7.3   \n",
       "\n",
       "   release_year    budget_adj   revenue_adj decade  \n",
       "0          2015  1.379999e+08  1.392446e+09  2010s  \n",
       "1          2015  1.379999e+08  3.481613e+08  2010s  \n",
       "2          2015  1.012000e+08  2.716190e+08  2010s  \n",
       "3          2015  1.839999e+08  1.902723e+09  2010s  \n",
       "4          2015  1.747999e+08  1.385749e+09  2010s  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Aggregate years into decades\n",
    "bin_edges = [1960, 1970, 1980, 1990, 2000, 2010, 2015]\n",
    "bin_names = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s']\n",
    "movie_data['decade'] = pd.cut(movie_data['release_year'], bin_edges, labels=bin_names)\n",
    "movie_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fac084018d0>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Draw the bar chart to compare the revenue in differet decades\n",
    "revenue_distribution = movie_data.groupby('decade').revenue.mean()\n",
    "\n",
    "plt.bar(revenue_distribution.index, revenue_distribution.values)\n",
    "plt.title('The comparison of revenue among decades')\n",
    "plt.xlabel('Decade')\n",
    "plt.ylabel('Revenue')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the bar char above, the revenue increased over the year. The 2010s accounts for the most, while the 1960s accounts for the least.\n",
    "\n",
    "Next, we need to find the pattern of the high revenue. To order to discover the pattern of the group of high revenues, it is defined that the high revenue is the revenue above the 75% percentile."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    2.711000e+03\n",
       "mean     1.534082e+08\n",
       "std      1.939356e+08\n",
       "min      2.414561e+07\n",
       "25%      4.480000e+07\n",
       "50%      8.636982e+07\n",
       "75%      1.772410e+08\n",
       "max      2.781506e+09\n",
       "Name: revenue, dtype: float64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extract the high revenue dataframe\n",
    "high_revenue = movie_data.revenue.quantile(.75)\n",
    "high_rev_df = movie_data[movie_data.revenue > high_revenue]\n",
    "high_rev_df.revenue.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, we need to discover the correlation between different variables. \n",
    "In this question, three variables will be selected:'popularity', 'vote_average', and 'budget'. \n",
    "The scatterplot and correlation calculation will be used to analyze these correlations. \n",
    "The first group to discover is the correlation between 'popularity' and 'revenue'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fac0a3e2748>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Draw the scatterplot of the popularity and revenue\n",
    "plt.scatter(x=high_rev_df.popularity, y=high_rev_df.revenue)\n",
    "plt.title('The correlation between Popularity and Revenue')\n",
    "plt.xlabel('Popularity')\n",
    "plt.ylabel('Revenue')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>popularity</th>\n",
       "      <th>revenue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>popularity</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.582073</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>revenue</th>\n",
       "      <td>0.582073</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            popularity   revenue\n",
       "popularity    1.000000  0.582073\n",
       "revenue       0.582073  1.000000"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate the correlation between 'popularity' and 'revenue'\n",
    "high_rev_df[['popularity', 'revenue']].corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The correlation between these two variables is 0.51, a relatively high figure. Then, the relationship of 'revenue' and 'vote_average' will be discovered."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEWCAYAAACJ0YulAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzt3XucXHV9//HXezcTshsgSyAoLCQRiqHEAIGUi6ktV6OgIVwFod6lWqz10miiVILFgr/Yipa2qEhRucjVCEoNWC4qGiCQhBggFggk2XAJhHDLQjabz++Pc2aYnT3fmTmTOTs7u5/n45FHds6cOfM9M2fO55zv5fOVmeGcc84BtDS6AM455wYPDwrOOecKPCg455wr8KDgnHOuwIOCc865Ag8KzjnnCoZ8UJA0T9KVjS7HttrW/ZC0QtIRdSxSfrt3SfpEvbfrmoukr0i6rNHlqETSFZIuaHQ5BrOmDwqSXi36t1VSd9HjMxtdvkZIOvDNbLKZ3dWgIiVqpoASl/VFSds1uizbStL3JP04Yfn+kt6QNLbC64+QtLZ4mZn9i5k1xXcZIukjknrjc8fLkpZJel+jyzXQmj4omNn2+X/AauD9RcuuanT5SkkaUc0yN3hImgi8CzBgZkbvMZDHwBXASZJGlyz/EPALM9swgGUZbP4Qn0s6gP8Efiqpo8FlGlBNHxSqNFLSjyW9ElejTMs/IWl3STdKWi9plaTPhjYiqU3Sv0p6StJLkn4nqS1+bma87Y3xVeWfF73uSUlflvQQ8JqkEYFlacpyvaRn4nL8RtLkePnZwJnAl+IrnluKynBM/Pd2ki6WtC7+d3H+Cjh/FSjpi5Kek/S0pI9W+Hz3lnRfXJafF19pSjpM0u/jz2VZvgpL0jeITrSXxOW8RNL5kv49fj4n6TVJ/6/os39d0k7lths/N0bSD+Oyd0m6QFJr/NxH4u/tW/GV/ypJ762wfx8CFhGdTD9csm/P5LcdLzsx/k6R1CJpjqTHJb0g6br8ZyNpoiST9HFJq4E7yn2v8XM7S7olvoq9P96v3xU9v6+k2yVtkLRS0mlJO2NmfwC6gJOLXtsKfBD4Ufw48RhRFEj+B9hdb96R766i6s2iffuwpNWSnpf01aL3apP0o/jzf0TSl1Ry51FM0nckrYn3+wFJ7yp6bl78uYZ+31MlPRg/dy0wKvQ+JZ/RVuAnwGhgn6LthY7n0yUtLin35yXdXPR5fiv+PJ6VdKnePHeU/c2p5I46fwwXPa7qe6+amQ2Zf8CTwDEly+YBrwPHAa3AhcCi+LkW4AHga8BIYC/gCWBGYPv/AdwFdMbbeiewHfB24DXgWCAHfAl4DBhZVK6lwJ5AW9KySmWJ9+PKorJ8DNghfv+LgaVFz10BXBD6bICvE53kdgXGAb8H/jl+7ghgS7xOLv7cNgE7BT6Tu4hOMO8g+gHdmC9n/Dm9EG+jJf58XgDGFb32E0XbOgpYHv/9TuBx4N6i55ZVud0FwPfi8uwK3Af8bfzcR4Ae4JPxd/hpYB2gMsfVY8DfAQfHr31L0XOPA8cWPb4emBP//bn4c94j/p6+B1wTPzeR6M7jx3E588dFue/1p/G/dmA/YA3wu/i50fHjjwIjgIOA54HJgX36KvDrosczgPVArspjZG3C7+zKkn37AdGxfQDwBvDn8fMXAXcDO8WfzUOl2yvZ9lnAzvF+fRF4BhhVxe97JPAU8HmiY/mU+Pu7IPA+Hyn6PFuBc4DNwK6Vjrv4O3kF2Kdoe/cDp8d/XwzcDIyNv99bgAur+c3R/3dSXM5U33tV59GBOmHX8x9wOfAc8MeS5U/SPyh8G9gQH3h3AUcC3fFzhwKrS9afC/x3wnu2AN3AAQnP/RNwXcm6XcARReX6WEJZP1b0uGxZKAkKJet1EP0Ix8SPryg98OkbFB4Hjit6bgbwZNEB2g2MKHr+OeCwwHvfBVxU9Hg/oh9SK/Bl4Ccl6y8EPhw42NuIfuA7A3OArwBrge2B84HvxusFtwu8hegE1Fb03BnAnfbmD+qxoufa48/urYH9+0uiE8ku8eNHgc8XPX8BcHn89w5EFwcT4sePAEcXrbtbvK0RvHni3KvMcV74XuPPsweYVPLe+ZPDB4Dflrz+e8B5gW2Pj7e3R/z4KuA7Rc9XOkaqCQp7FD1/H2+eIPtceAGfKN1ehd//i8S/w/h9i4Pbfrz5+/4rSgI+UXArFxS2ABvjz6YbOK3o+UrH85XA1+K/9yEKEu2A4uNi76LXHQ6squY3R/mgkOp7r+Zfs1YfXQG8p8p13w08amb7E0XivwdGKarDnUB0G7wx/4/oRPSWhO3sQnTr+XjCc7sTXZEAhVvPNURXFnlrEl5XvKzqskhqlXRRXC3xMtEJP1/GavQpb/z37kWPXzCzLUWPNxGdmEOK9+MpoqudXeJ9OrVkn/6S6OTYj5l1A4uBvyb6Qd9N9COeHi+7O1613HYnxO//dNFz3yO64s17pug9N8V/hvbvw8BtZvZ8/PhqiqqQ4scnKap+Owl40Mzyn+0E4GdF5XgE6KXvd1r47Cp8r+OIgsmapNfG73VoyWdyJvDWpJ0ys9XAb4CzJG0PzCKuOopVOkaq8UzR38XH0O5l9qOfuFrlkbhKbSNRkCw+1kvfJ//73h3osvhMGSvepySLzKyD6C7mZqIqzrxKx/PVRBcgEFXFLYiPr/ydxANFr/tVvDwv7W+uuExVf+/VaMoGTjP7jaLGvwJJexP92P5T0rPAJ83sUaIPfmW82p3Az4tetoYoWu9DZc8TXcXuDSwreW4dMKWoLCKqFuoqLnbSrtRYlg8CJwDHEJ04xhBdPanMe5WWdwKwIn48Pl5Wqz2L/s5fgT5PtE8/MbNPBl6XVM67iaqKphLdft9NdJV6CNFJjHLblbQb0Z3CLiU/stTiOt/TgFZJ+RPPdkCHpAPMbJmZPSzpKeC9RN/L1UWbWEN0N3hPwrYnxn8Wfwblvtf1RFexewB/itcv/tzXAHeb2bEpdvFHRHdkTxMdew8WPVfuGKl0fFXyNNF+PBw/3jO0Ytx+8GXgaGCFmW2VVHysV3qfTkkqCgzjSb6w68PMXpX0d8Djki43syVUPp5vA3aRdCBRcPh8vPx5ojuByWbWFXhtOa8RBZW84hN+Ld97Wc16p5Dk+0T1e38H/CNRzwGAZ3nzoDuRvtH3PuBlRQ2+bfGV2jsk/UXpxuOr/8uBf4sb1lolHR5fIV4HHC/paEk5onrPN4iucqtVdVmIqineiPe3HfiXkuefJWqTCLkGOFfSOEm7ELVjbMtYjrMk7Sepnehu7AYz6423+X5JM+L9GRU3qu1Rppx3EzXsPmxmm4lvnYlOWuvjdYLbNbOniX6c/yppR0WNvXtL+usa9msW0ZX9fsCB8b8/B34blzHvauCzRHc31xctvxT4hqQJAPHnfUKZ9wt+r/HneRMwT1K7pH1LyvAL4O2S/kZRI31O0l+oqMNDghuJfhvn0/cuAcofI88CO0saU2bb5VwHzJW0k6RO4DNl1t2BKBiuB0ZI+hqwY5Xv84f4tZ9V1JHjJKKLi6qY2QvAZUT7DhWO5/gi5AZgPlHbwe3x8q1E7SvflrQrgKROSTOqLMpSorvRdkl/Bny86LlavveyhkRQiG9/30lURXApUXVB/pbuNuAtkpYQVUEUVx30Au8n+rGvIorolxFdoSX5R2A50RXsBuCbQIuZrSRqDPv3eBvvJ+oau7nafUhZlh8T3QZ3EV1tLSp5/ofAfvHt5IKE119AVE3zULw/D8bLavUToiq9Z4iq2D4b79MaoivfrxD9qNcAs3nzuPsOcIqiXijfjZf9nqhtIX9X8DDRHVr+cTXb/RBRI+PDRFfaNxCosqrgw0RtOqvN7Jn8P+AS4Ey92Y30GqJ64TuKqpny+3czcJukV4i+p0PLvF+l7/UzRMfDM0Sf+TVEQQQze4WoqvR0oiv6Z4iOz+C4CjN7jTcDQ2n37eAxEt+BXwM8ER9jaauVvk7UVrQK+DXR9/NGYN2FRL2d/kT02bxOheqmvPj3dxJRHfyLRPXvN6Us68XAcZL2r+K4g+gC4Rjg+pI71S8TdVhYFFcN/hqYVGUZvk3UTvcsUfAufFe1fO+VqG91W/OIb79/YWbvkLQjsNLMyv7w4+DxqJntUW4955qBpG8SNZB/uOLKg5ikTxM1QtdyN+fqbEjcKZjZy8AqSadCVKcv6YD4710k5fdzLlEVkHNNR1F/9P3j4/sQomqEnzW6XGlJ2k3S9LhqbxJRdWvT7cdQ1ZRBQdI1RPWFkxQN+vg4UYv7xyUtI2ocy9fdHgGslPQnoobobzSgyM7Vww5E1R+vEdXL/yt9O040i5FEVbyvEA3a+zlvtgG6Bmva6iPnnHP115R3Cs4557LRdOMUdtllF5s4cWKji+Gcc03lgQceeN7MxlVar+mCwsSJE1m8eHHlFZ1zzhXEgywr8uoj55xzBR4UnHPOFXhQcM45V+BBwTnnXIEHBeeccwVN1/vIOdd8FizpYv7Clazb2M3uHW3MnjGJWVM7K7/QDTgPCs65TC1Y0sXcm5bT3dMLQNfGbubetBzAA8Mg5NVHzrlMzV+4shAQ8rp7epm/cGXgFa6RPCg45zK1bmN3quWusTwoOOcytXtHW6rlrrE8KDjnMjV7xiTacq19lrXlWpk9o9qJx9xA8oZm51ym8o3J3vuoOXhQcM5lbtbUTg8CTcKrj5xzzhV4UHDOOVfgQcE551yBBwXnnHMFHhScc84VeFBwzjlX4EHBOedcgQcF55xzBR4UnHPOFXhQcM45V+BBwTnnXIEHBeeccwWZBQVJe0q6U9IjklZI+oeEdY6Q9JKkpfG/r2VVHuecc5VlmSV1C/BFM3tQ0g7AA5JuN7OHS9b7rZm9L8NyOOecq1Jmdwpm9rSZPRj//QrwCOC5c51zbhAbkDYFSROBqcC9CU8fLmmZpP+RNDnw+rMlLZa0eP369RmW1DnnhrfMg4Kk7YEbgc+Z2cslTz8ITDCzA4B/BxYkbcPMvm9m08xs2rhx47ItsHPODWOZBgVJOaKAcJWZ3VT6vJm9bGavxn/fCuQk7ZJlmZxzzoVl2ftIwA+BR8zs3wLrvDVeD0mHxOV5IasyOeecKy/L3kfTgb8BlktaGi/7CjAewMwuBU4BPi1pC9ANnG5mlmGZnHPOlZFZUDCz3wGqsM4lwCVZlcE551w6PqLZOedcgQcF55xzBR4UnHPOFXhQcM45V+BBwTnnXIEHBeeccwUeFJxzzhV4UHDOOVfgQcE551yBBwXnnHMFHhScc84VeFBwzjlX4EHBOedcgQcF55xzBR4UnHPOFXhQcM45V+BBwTnnXIEHBeeccwUeFJxzzhV4UHDOOVfgQcE551yBBwXnnHMFIxpdAOecq4cFS7qYv3Al6zZ2s3tHG7NnTGLW1M5GF6vpeFBwzjW9BUu6mHvTcrp7egHo2tjN3JuWA3hgSMmrj5xzTW/+wpWFgJDX3dPL/IUrG1Si5uVBwTnX9NZt7E613IV5UHDONb3dO9pSLXdhmQUFSXtKulPSI5JWSPqHhHUk6buSHpP0kKSDsiqPc27omj1jEm251j7L2nKtzJ4xqUElal5ZNjRvAb5oZg9K2gF4QNLtZvZw0TrvBfaJ/x0K/Ff8v3POVS3fmOy9j7ZdZkHBzJ4Gno7/fkXSI0AnUBwUTgB+bGYGLJLUIWm3+LXOOVe1WVM7PQjUwYC0KUiaCEwF7i15qhNYU/R4bbys9PVnS1osafH69euzKqZzzg17mQcFSdsDNwKfM7OXS59OeIn1W2D2fTObZmbTxo0bl0UxnXPOkXFQkJQjCghXmdlNCausBfYserwHsC7LMjnnnAvLsveRgB8Cj5jZvwVWuxn4UNwL6TDgJW9PcM65xsmy99F04G+A5ZKWxsu+AowHMLNLgVuB44DHgE3ARzMsj3POuQqy7H30O5LbDIrXMeCcrMrgnHMuHR/R7JxzrsCDgnPOuQJPne2cG5R8foTG8KDgnBt0fH6ExvHqI+fcoOPzIzSOBwXn3KDj8yM0jgcF59yg4/MjNI4HBefcoOPzIzSONzQ75wYdnx+hcTwoOOcGJZ8foTG8+sg551yBBwXnnHMFHhScc84VeFBwzjlX4EHBOedcgQcF55xzBR4UnHPOFXhQcM45V1B1UJA0QdIx8d9tknbIrljOOecaoaqgIOmTwA3A9+JFewALsiqUc865xqj2TuEcYDrwMoCZ/R+wa1aFcs451xjVBoU3zGxz/oGkEYBlUyTnnHONUm1QuFvSV4A2SccC1wO3ZFcs55xzjVBtUJgDrAeWA38L3Aqcm1WhnHPONUZVqbPNbCvwg/ifc865IaqqoCBpFQltCGa2V91L5JxzrmGqnWRnWtHfo4BTgbH1L45zrh4WLOlq+lnLhsI+NKOq2hTM7IWif11mdjFwVLnXSLpc0nOS/hh4/ghJL0laGv/7Wg3ld86VWLCki7k3LadrYzcGdG3sZu5Ny1mwpKvRRavagiVdzL5hWZ99mH3Dsqbah2ZV7eC1g4r+TZP0KaDSiOYrgPdUWOe3ZnZg/O/r1ZTFOVfe/IUr6e7p7bOsu6eX+QtXNqhE6Z1/ywp6evvWWPf0GuffsqJBJRo+qq0++teiv7cATwKnlXuBmf1G0sSaSuWcq9m6jd2plg9GL27qSbXc1U+1vY+OzOj9D5e0DFgH/KOZJV4GSDobOBtg/PjxGRXFuaFh9442uhICwO4dbQ0ojWs21fY+2g44GZhY/JptrPJ5EJhgZq9KOo4ol9I+SSua2feB7wNMmzbNR1I7V8bsGZOYe9PyPlVIbblWZs+Y1MBSpdPRlmNjd/+7go62XANKM7xUO3jt58AJRFVHrxX9q5mZvWxmr8Z/3wrkJO2yLdt0zsGsqZ1ceNIUOjvaENDZ0caFJ01pqp4782ZOJteiPstyLWLezMkNKtHwUW2bwh5mVqnROBVJbwWeNTOTdAhRgHqhnu/h3HA1a2pnUwWBUvmye5fUgVdtUPi9pClmtrzaDUu6BjgC2EXSWuA8IAdgZpcCpwCflrQF6AZONzOvGnLOAeHA5uMXslVtUPhL4CPxyOY3AAFmZvuHXmBmZ5TboJldAlxSbUGdcy4/BiPfXpIfgwF4YKiTaoPCezMthXPOVaHcGAwPCvVR7Yjmp4A9gaPivzdV+1rnnKuXoTAGY7CrdkTzecCXgbnxohxwZVaFcs65JKGxFj4Go36qvdo/EZhJ3A3VzNZROc2Fc87V1ewZk2jLtfZZVusYjAVLuph+0R28bc4vmX7RHZ5XKVZtm8LmuOuoAUganWGZnHMuUb26qnqDdVi1QeE6Sd8DOiR9EvgYPuGOc64B6jEGwxusw6rNffSteG7ml4FJwNfM7PZMS+accxnxBuuwanMffR643gOBc26wSjOozZMGhlXb0LwjsFDSbyWdI+ktWRbKOefSSDuxUD0brIeaascpnG9mk4FzgN2BuyX9OtOSOedcldJOLDQUkgZmpdqG5rzngGeIEtftWv/iOOdcerW0ETR70sCsVDt47dOS7gL+F9gF+GS5vEfOOTeQfFBb/VR7pzAB+JyZLc2yMM655jDYMpUOhYmFBotq2xTmANtL+iiApHGS3pZpyZxzg1LaRt2B4G0E9VNtl9TzgGlEYxT+mzdzH03PrmjOucFosA788jaC+vDcR865VHzg19DmuY+cG4KyrPP3gV9DW7V3CqW5j34NXJZdsZxztcq6zt8Hfg1tnvvIuQbI8ko+6zr/emUqbTaDrcdVVqoevBYHgdsBJLVKOtPMrsqsZM5lrFE/8qzTNtezzj/0GQ23Rt3hlGq7bPWRpB0lzZV0iaR3K/IZ4AngtIEponP118hulWlTMqRVr4Fcg7HraaNk/Z0NJpXaFH5CVF20HPgEcBtwKnCCmZ2Qcdmcy0wjf+RZ996pV51/s50Is5xJbTj1uKpUfbSXmU0BkHQZ8Dww3sxeybxkzmWokT/yrHvv1KvOv5lOhAuWdDH7hmX09BoQ3dXMvmEZUJ/qneHU46rSnUJP/g8z6wVWeUBwQ0Ejc+UMRO+dWVM7uWfOUay66HjumXNUTSfGMW25VMsb6fxbVhQCQl5Pr3H+LSvqsv3h1OOqUlA4QNLL8b9XgP3zf0t6eSAK6FwWGvkjb5aUDFK65Y304qaeVMvTapbvrB7KVh+ZWWu5551rVo3uVpm29865C5Zzzb1r6DWjVeKMQ/fkgllTMiwhbAycUEPLh7rh0uMq7XwKzg0ZzfIjP3fBcq5ctLrwuNes8DjLwFCuHn2w9dnvaMuxsbt/sOoYhFVdg121I5pTk3S5pOck/THwvCR9V9Jjkh6SdFBWZXGumV1z75pUy+slVMV25L7jBl1X1XkzJ5Nr6VuvlWsR82ZOblCJsu0NlaXMggJwBfCeMs+/F9gn/nc28F8ZlsW5ptVrlmp5vYTq0e98dP2g66o6a2on8089oE9Z5596QMPuXpp5jEdm1Udm9htJE8uscgLwYzMzYJGkDkm7mdnTWZXJuWbUKiUGgNYBaPFNqmL7/LXJc22t29idulqpntVQg6k6cLCmF69GI9sUOoHi+9+18bJ+QUHS2UR3E4wfP35ACufcYHHGoXv2aVMoXp61pJN2qK1hTFsumAoC+jfqAzWljmhk4KlWM43xKNXIoJB0mZN4P2xm3we+DzBt2rRs75mdG2TyjckD3fsolO/n5IM7ufGBrn5TX0okXh2ff8sKXu/Z2m87o3Itqa+m0+YgalTOomYe7JZlm0Ila4HiS509gHUNKotzg9q0CWN565hRCHjrmFFMmzA28/cMVYHc+ej6xLaGUFfVFzf1JG4nNIYgfzJNaqhNm3qjllQd9WggbubBbo28U7gZ+IyknwKHAi95e4Jz/dVytVuPKpNyVSBJ9ffzF65MvDpOq1UK7nPpCb6asqZZXq87i0aPg9kWmQUFSdcARwC7SFoLnEc0tzNmdilwK3Ac8BiwCfhoVmVxrpmlbbSs14ktbRXI7BmT+p2423KtbDeiJXEMQUivWXCfRXIdcyj1Rtp9qGcD8WBq+E4jy95HZ1R43oBzsnp/57Iw2Botk8pTrxNb6CQfqgIJXR0DidsZlWtJrELqDJzIIdDoSDj1Rtp9aOYG4nrxEc3OVWkgGi2T0lmErnY72pN7+6StYgmppQqk3NVxUrAozmwKkGsVs2dM4ovXLUs1DiPUnpF2H5q5gbhePCg4V6Ws+56H0llM33ssG17b3O9q1yy5t09oXEMtJ7Z6VYEkbWfBkq7+l/7x47QD88rtW5p9OHLfcYndf4/cd1zwNYMt5ce2amTvI+eaStZVC6G0FYueeDGxt89LgXr6XrOG9XxJ03Nn/sKV9GwtSXe9NWpP6Ayc5NtzyaesciftNO58dH2q5c08cjnE7xScq1ItVQuhq8ik5eXSWaTp7dNZ1LYwkFevaavXygXZb3/gwMS2AAu0Kvxi2dN1GbfRqPabwcSDgnNVSttoGTpJLn5qQ5/BX/nloZ41oXQW5coTqjLJMgV32hNkuSAbagv4XCDFRpreTeU0qv1mMPHqI+eqNGtqJycf3Fk4SbdKnHxw+YbVpJPkNfeuSVzePjJ5+pJQOou0E7/k2yzydyT5NotzFyxPXD+ttNVrlQZ41WP2uLRCZSrXfpOkmRumPSi4YSvtyNUFS7q48YGuPifVGx/oCr4udDIMVRNt2tzLWYeN7xN0zjpsfN2u5LNOwZ12itO0QRZgp/bk8Qih5eUkff+hQDsY22+y4tVHbliqZaL3elWPlOsddMGsKVUHgbR1+Fmn4K6lei0pyE6bMDb4HRy//26JvYOO33+3VGWt9NkN9vabLPmdghuWapnovV7VI2ccumddri5ryeuTpXpVr5Urf9reQSFp33vizsl3OxN3bmtINVeW/E7BDUu1TPSetvfRrKmdLH5qQ5+G3ZMP7uSCWVOYNmHsNl9dhkb9dgV6ymRtwZIurr1vTZ8r/2vvWxO88q+li28tr0n6LNJuZ9ETL6Za3sw8KDhXpXpXj2zrFWWotxIkz1PQnmthU8/WfuvWUh+fZN7NKxLHHcy7eUXq3kchaV+zYEkXs69fVihX18ZuZl+/jI72XOIFQGg7jZr9rhG8+sgNS6EJ3ctN9J62t0/W1TvlTkdJ79udEBAAXg90q0wr1C00tLyW9NKzZ0wi11oyF3OcGiNJKFC93tOb6r1DvYwGYva7geZBwQ1L82ZO7nfwt8TL62WwJVcLBZFQsMha2iCb11tyki99XCwUkLp7tqZ671C34IGY/W6gefWRG7ZaW8XWosbm1tbyV33leqxA/4FWWSdXK1d9lFY9BrXtFKiSKVc9lbYa7fxbVlAaA7ZatDzL1NaNmv2uEWRNVic2bdo0W7x4caOL4Zrc9IvuCHYxvGfOUales1N7rs90kxBVRYSmrazmargapQn0CuXceywPrn6p3/uGRt+GpB0jUdrNF6KqnfmnHADUZ8KZiXN+GXzu4g8cWPUIaIAnLzo+9funMdgS5Ul6wMymVVrPq4/csFTPni+h6SZD01bW68RwwawpTN+777Sc0/cey1WfPDyxa2haaQe1zZrayfxTDuizv/mAMBBJ45Leoy2QQK9c21E9NHOiPK8+csNSPXu+hISmrayXBUu6uO/Jvl0i73vyRc5dsJxr7y/pGnr/mtTVTbX0rEna3+kX3VFT0rikK+2OtlxiO4FIblzfqT3Hll7r09ica1HZtqN6XOE3c6I8v1Nww1KtPV+SXhO66sw6/01oAN5Vi1YnLk97is/Plbytk9hXyjyatP3Qlfb7DtiNXEtJ76MWBfdt46Ye5p9acvdy6gFl57auxxX+YOtkkIbfKbhhqdZZxZJeA8nTTc6eMSlV6uy0V5ChgXb1aiU8bK+dMp3reUxbcuZRCF9p3/noeuafekBiCutyGVerLW8tV/hJ32Uzz+DmQcENW7VU7aSdbjKUOvva+9ck5l1K2k7W1Q07tec4fv/d+vWsufPR9XWpAgnNZtbTuzW4/XKjtUPfQZqBhVCfkc6hHmmhTgbNkCjPg4JzGQlddV597+p+3Sp7eo2v/mw5W4tSNFe6Mg/Vr6dlBtMmjOWYReLnAAAXIUlEQVTOR9ezbmM3bx0zimkTxiaeyPPlSuMXy55OXP7a5vBcBKGkgaHBYuXu/EIpP5JO5mMCn2noCr/cHc2FJ00ZVL2PquVdUp3bRqVXi1BbF9CQUDfZ0hQOENWvf+CQPbn2vjX9lpeO7C1WWt62XCuvb+kl6fTQKvH4hcdVXf5y3UiTdFZo0E/TlTT03YzKtQTHVCR1Lw71GnvbnF8mVtcJWJVxl9e0vEuqG7JqmQdhWxtLywldLbbUKQNC6AQ5a2pnYiPqBbOmJC4PzXvcKiWWP3S9WM98P6HG/lD2iLRZJULfTag9ZuOmnlSZXtPOIdEMvPrINZW0cwikXb+SpJG/ofrmMhfmqZTLr3P94tWFoNG1sZvrF68u1LlXW+9eyx1NvQZmhapYQoPO0sajtL19xrTlUs3xkDZJYjPwOwXXVNImmatnUrrQdJahAVLlJOVdCgldmZ/5gz9wz+Mb+iy75/ENnPmDPySuH5rvIHQHUU6abpv1nC2tnKQ7wtAVe0dbLvEuRUoe7xA6XmqZPW6w86Dgmkra3iH17C8eGuHbvWVrqvELHW25fnmWWlsVXD900i4NCJWWh1J5H7nvuMS+/+VqakInzqQTc2hWtP1226Fuo37z7SvF25p9/bLgvs2bOTlxtPnGQLVSud5HaaZobQZefeSaStr+3/XsLx66YjdLrgaB5OoaicTBZT29ydlKj9x3XOqyJgndNf1i2dP99q3XjBEtkCaBav6kXlpVNypwJ7XoiRf7vW8+uIR6VoUCZyhF9o0PrKVfdIsfp5l2M23vo2YYuRyS6Z2CpPdIWinpMUlzEp7/iKT1kpbG/z6RZXlc80s7Ernc+mkboNPm1A+lhg41coa6aKadahKSq1JCV7sbu3sSM4/WklE7TaNuKMiu29hdNrV50r6VS5GdFIBD1UFpj69mHrkcktmdgqRW4D+AY4G1wP2Sbjazh0tWvdbMPpNVOdzQknYkcrWjkKtpgD7j0D0T++5XGvlbur0vXrcsVQ+efDqI0n3IBa7kWwVfuHYp+ae6NnbzhWuXBmcba5TQWIT8VXlSavPFT23oMyisNH15tUKfadrjq5lHLodkWX10CPCYmT0BIOmnwAlAaVBwLpW0I5HrlaRt2oSxXL1oNcXn4Rbg4adfSbWttF06x7Tl+qSkzo+A/sAh4xODVIugp/TKH3j19Z7E8Qj1Gk8REgpee41r5/+ee63f8iP3Hcf8hSsTr/DzPb+K5bv/JvX2Ci0vl2IjDe99lE4nUNwytzZeVupkSQ9JukFS4jRGks6WtFjS4vXr099KO1eqltv++QtXUnpu20o4B1Eo4Vuo183oka2JVRc9vclVIL986GnOOmx8n54vZx02Pljt07OVxJ4y9e4FVGpLoDxPrN+UuPzOR9cHx2aEAmqo++/he41N1cvo/FtWpGr8rnX2uMEssxHNkk4FZpjZJ+LHfwMcYmZ/X7TOzsCrZvaGpE8Bp5lZ8gwnMR/R7OrRR76WSXZCo1dDQqNjwRKnwOxoyzFv5uRUE8WkvfJPWv/kgzv75GKCaHKc0kA0UAS0BKqW0uosSphX7Wca2k7ouGgW1Y5ozrL6aC1QfOW/B7CueAUze6Ho4Q+Ab2ZYHjcE1GswWi23/W25FjYlnMxboN8dBMAbPb39Tv7lTtgvdfckVnWVO4ElXe2WE8w8ekr/zKNpT5z1MirXUrd5o0NzWtTSrjNcZFl9dD+wj6S3SRoJnA7cXLyCpOIOzDOBRzIsjxsC6jUYrZbb/qSAAMkBodz6IeUGWmUpdMLL+n1D3tiylfYaBgQmCX2mae9CmrnhOK3M7hTMbIukzwALgVbgcjNbIenrwGIzuxn4rKSZwBZgA/CRrMrjBq801UH17AIYarDOem7d0Axo7SNbEt978u47BAek1UOo0fXkgztTJ9arh60WDQhMY59dR7P2xderntMi1POpRbDdiP5VbM3ccJyWZ0l1DRXK9BmaHauWtoC05UmqVrrwpCkDUp2SZe+g9lxLNEiu5LPeftSIxMbyUH182qqXkFBwDJ2wy+nsaOPIfcf1y0s1bcLY1PmezjpsfL/tXDBrSuYXC1mrtk3Bg4JrqAPPvy04cnXpee/utzyff6jUWYeNZ9qEsal+tEk/8tCI1krpnJvB9L3HsmjVi/QWBYXWFvV5XCyU/jltKuyd2nPst1vfu53pe4/lbeO2D36XSXNOVFLaOJ5rFaNHjkg8vkKBp6Mtxxtb+ncOCDXGzz8lPLXnYDMYGpqdqyg0EjW0PDS695cPPR0c1LT4qQ2JV5DFdyj5XDmhqpFmDwiQnBMpFBAgqlZKCpyhvv8h++22A/eterHPsvtWvcip08azav2r/YLFBbOmcHVggp+QUOqQ0HEUuhMJzQYXmhjp/FtWNE1QqJYHBTdgQjNgpRFqO0iq/uju6eWrP1veJ31EPrPpdfevScyVE1KpSqMRg8Ky1t3Tm9jWkPYK/vdPbOiX8rpnqzH3pocoTUz04OqXWLCkK9h4H1KvCo9QqpHQPg+mEeL14kHBDYhQV9LRI1sTf4g7tSdfpYbSCoSEfuSbU/bBr1THfdD4MX2ueEsfN6M3Ehp7awl0oY8uqdtprWnNXf14UHAV1aOBLdSVtKMtR651a7+62uP33y3VhOjbjWipy3zFIZXaFJLmNXC16drYnbqKqp6S7vq29PYmjhQvN5dGszZM+3wKrqz8Ff625rwPVfu81N3D/FNKpo485QDufHR92QnRS8cXvO+A5Jz99TJx57a69Z13lX3w0PGJy7cbke47CM0JEVo+emRrYiqQ7Uclj9kYVZJCI69ev5tG8KPclVWvwWJp57INXZWHlteSXjqNex7fwEkH75Hpe7g3TZswtt8c1y0i9bzXI1qiO89iuVYF53iweJKc0klzys3pnJTfqp4z/g0075Lqygrl+wl1VwwJ9f8PVQe9saU3sfpAwIiErocDkadnKHRLbRb1/KxL05CE0pKUE+poEMpvFWp7Sfu7qSfvkupSS9Owm3bYfyhPfeiKKsRI7no4EIZT/ptGq+dnnZTZNq1QR4PXA/mtKs0VMZj5nYID0l/JX3jSFKD6yUhC0mYebaTQFJGuvjo72ti0eUtilc3oka1RGoyS47FF4Z5m9VDLKOukButy+bUyT69S5Z2CtykMYWmmmwxdsYcadoHUDWlJ5RnToKRrtQjNoexql1TfP3vGpGA31lxrS+Lx+I0TpyRuK62d2nOJ8y/UknYjTcLFwdQw7UFhiEp7kJVLNDdraif3zDmKVRcdzz1zjmLW1M7UDWmh8jTTAK8sr0SHrdJzbfz4pcAdWWj5rKmdib3Y0jp+/90ST+ahiYhCvaGO3HdcqvcdTA3T3qYwRJU7yJKuVtK2HaTNVpq27cAND0mjyucvXBk8Hjvaw9NoLn5qA8+89DoGPPPS6yx+akNwcGQoGd+dj67ngln9r+jn3bwisfybA9lcf7EsnHYl6fdXz+y/28rvFIaotAfZ7BmTEm+bQ6ko0nYxrefBndRV0Q0dXRu7g8ejWfJEQXNveogrF63u05X0ykWr2bwl+cIjVBkU6vEUukMJbWdjd0+qK/+0v6cseVAYotIeZGknnQndHh+57zjOXbCcvefeysQ5v2Tvubdy7oLldW07KK3ebbK+Eq4CET4eQyfn0ExtaSdwyw9aK9URqD4KrB5Ur4uyLHn10RA1e8YkvnDd0j59/VtE2YMsNOlMktBgsZ892JWYgC7tSNRyAtXQbojIf59Jx2MotXm9hBqU3whUdeZaRGtLS79eRqNyLYm9p8pdlMG29+arBw8KTSJtd7XFT23oN/hrq0XL0x5oSe8d+mGGGmOTkqs5l1b7yGwrN0JTkIamVt3ca1x8ypTE7L9p5wBPc1GWJQ8KTaCWyeqvuXdNcPkFs6akeu+keQecy9qh37idZ1/ZXHj8lh1G9nmchbTVQVD+ZD4YrvzT8qDQBNL2JILwbXDa/tbzbl6Rat6BckozXzYyE6Yb3EoDApB5QIAol9G5C5b3m5QpNHCxIzARUT5QNEMQKOVBoQnU0l0tNAKzVUpVFVXPEbxJ1VnOJRmIAJCkfWRrnylC821i++w6OvG3MHn3HcreSfudwiDWLLnN65V/6LC9dkrM6b/XuPbUVVHODUVJd66hNrH/e+61xOW/f3xDv44OPVuNr9z0EIaa8nc2LIJCLXXyA1GmSo1T+XIeNH5MYlDIdwtNut198oXku4gn1m/qdweRr4pKmsvYuaGqHneuoZckNUxXqvIdLIZFQrzpF92ReFLt7GjjnjlH1atoVQslnwt1YwtVBXV2tHHkvuP63O7W24gWsSXh1xIaEeqcC/PU2YNEPYeQp62GOvMHf+hTjTN977E8+UJ3YsNxKO1DqHF43cZurro3u4AAJAYE8IDghp9ci/p0ssi1iJEjWpLTaCh5UGUzpM4eFkGhljr5NNU7eaXrX794dV3m7g0dYB3tueCMUM65+iq9OOs148A9xyT+pv9s3OjEdoi0ifIaYVhUH4Wqa0JpHEr75kN0VbD9qBGJJ+G0sy+F5FpgRGv/HOy9W7eyOWEimfZcS3BQjXNu8KmlyrpenWQGxXwKkt4jaaWkxyTNSXh+O0nXxs/fK2liFuVIm9cn1Dc/dFX+4qbk5Fdp9WwlsZxJAQHCoyydc4NT2irrRsyzkFn1kaRW4D+AY4G1wP2Sbjazh4tW+zjwopn9maTTgW8CH8iiPGkGkjRydq2kcn7u2qUNKo1zrp7StinUMnB1W2V5p3AI8JiZPWFmm4GfAieUrHMC8KP47xuAo6VaBpoPnKRMhqF8Kbk6fbqh7YeWO+caSySfK9JmPW3EPAtZBoVOoDgBz9p4WeI6ZrYFeAnYOcMyVSU0y9JO7bnE6p15MycnHgDzTz2Q6XuP7bN8+t5jGT2y77p5oeXzZk4mVzJpQK5FzJs5OfiatEKReFBHaOcGSOh3EMr+e+Zh41NVWYc0Yp6FLHsfJX2OpZXj1ayDpLOBswHGjx+/7SWr4Lz3T2b2DcvoKarLz7WK894/OXXyq1BD9hevX0ZvUbtFa4v4xonJieoqpdVN2tZhb0se0XzWYeO5fcUz/RKN3fvVYzn23+7q02Nin11Hc/sXjkhMTDb3uP34wrVLKW7VaAG2366Vl9/o356yY2B51knORrWK1xPaZEYItjRXH4thY59dRwPJo4hDx9FZh43nhvvX9PmuR7WKgycm/w722XU0j69/rd+I5g8eOp5r71/T77f/gb/YM3H5N0/eP3HQZz7p5LZW8cyeMSl1ttVtlVnvI0mHA/PMbEb8eC6AmV1YtM7CeJ0/SBoBPAOMszKFqqX3US2yTotRz+2HtpU00jlNhtRa3zcpiNz71WOD64eC0f7n/arPCWDH7Vp56Pz3sO9Xb+3343/0G8cFt5M0VuSqTx4eLOfEOb/st69PxgOOQs81y/K0n2loO2+b88s+V2/5QVmh7YTWD31nQPC5tMd16PsPHY9pl2dtoHsfZRkURgB/Ao4GuoD7gQ+a2Yqidc4BppjZp+KG5pPM7LRy2x2ooOCcc0NJw0c0m9kWSZ8BFgKtwOVmtkLS14HFZnYz8EPgJ5IeAzYAp2dVHuecc5VlOqLZzG4Fbi1Z9rWiv18HTs2yDM4556qX7dx2zjnnmooHBeeccwUeFJxzzhU0XUI8SeuBpxpdjjraBXi+0YUYYL7PQ99w218Y/Ps8wcwqpmltuqAw1EhaXE03saHE93noG277C0Nnn736yDnnXIEHBeeccwUeFBrv+40uQAP4Pg99w21/YYjss7cpOOecK/A7BeeccwUeFJxzzhV4UGgwSa2Slkj6RaPLMhAkPSlpuaSlkoZ8ultJHZJukPSopEfilPJDlqRJ8Xeb//eypM81ulxZkvR5SSsk/VHSNZJGNbpM28LbFBpM0heAacCOZva+Rpcna5KeBKaZ2WAe5FM3kn4E/NbMLpM0Emg3s42NLtdAiOdp7wIONbOhNOC0QFIn8DtgPzPrlnQdcKuZXdHYktXO7xQaSNIewPHAZY0ui6s/STsCf0WUIh4z2zxcAkLsaODxoRoQiowA2uI5ZNqBdQ0uzzbxoNBYFwNfgj6zWg51Btwm6YF4mtWhbC9gPfDfcRXhZZJGN7pQA+h04JpGFyJLZtYFfAtYDTwNvGRmtzW2VNvGg0KDSHof8JyZPdDosgyw6WZ2EPBe4BxJf9XoAmVoBHAQ8F9mNhV4DZjT2CINjLiqbCZwfaPLkiVJOwEnAG8DdgdGSzqrsaXaNh4UGmc6MDOuY/8pcJSkKxtbpOyZ2br4/+eAnwGHNLZEmVoLrDWze+PHNxAFieHgvcCDZvZsowuSsWOAVWa23sx6gJuAdza4TNvEg0KDmNlcM9vDzCYS3WbfYWZNfYVRiaTRknbI/w28G/hjY0uVHTN7BlgjaVK86Gjg4QYWaSCdwRCvOoqtBg6T1C5JRN/xIw0u0zbJdDpO50q8BfhZ9NthBHC1mf2qsUXK3N8DV8XVKU8AH21weTInqR04FvjbRpcla2Z2r6QbgAeBLcASmjzdhXdJdc45V+DVR8455wo8KDjnnCvwoOCcc67Ag4JzzrkCDwrOOecKPCi4piXpREkmad9Gl6WceHzGC5LGlCxfIOm0Mq87QtI7ix5/StKHsiyrcx4UXDM7gyhD5en12Fic1bPuzOw14DZgVtF7jQH+EiiXMv0IikbHmtmlZvbjLMroXJ4HBdeUJG1PlCrk4xQFBUnXSjqu6PEVkk6O562YL+l+SQ9J+tv4+SMk3SnpamB5vGxBnLBvRXHSPkkfl/QnSXdJ+oGkS+Ll4yTdGG/7fknTE4p8DX2D14nAr8xsk6Sx8Xs+JGmRpP0lTQQ+BXw+npfgXZLmSfrH+D3vkvRNSffFZXpXvLxd0nXxtq6VdK+kadv+ibvhwkc0u2Y1i+ik+idJGyQdZGYPEuWR+gBwazyK+Gjg00TB4yUz+wtJ2wH3SMpnszwEeIeZrYoff8zMNkhqA+6XdCOwHfBPRLmLXgHuAJbF638H+LaZ/U7SeGAh8Ocl5f0VcJmknc3sBaIA8e/xc+cDS8xslqSjgB+b2YGSLgVeNbNvAUg6umSbI8zskDgInkeUh+fvgBfNbH9J7wCW1vDZumHMg4JrVmcQpR6HKBCcQZRq4H+A78Yn/vcAv4knP3k3sL+kU+LXjAH2ATYD9xUFBIDPSjox/nvPeL23Aneb2QYASdcDb4/XOQbYL07fAbCjpB3M7JX8AjPbLOlm4JQ4yBxIVKUEUTXSyfF6d0jaubT9IeCm+P8HgIlF2/pOvK0/Snqoiu04V+BBwTUdSTsDRwHvkGRAK2CSvmRmr0u6C5hBdMeQT8om4O/NbGHJto4gSmld/PgY4PC4aucuYFT8+pCWeP3uCkW/Bjg33tbP46ya+bKVqib/zBvx/728+VsuV07nKvI2BdeMTiGqYplgZhPNbE9gFdFVMkR3Dh8F3kVUlUP8/6cl5QAkvT0w4c0YouqXTXGvpsPi5fcBfy1pp3iGrZOLXnMb8Jn8A0kHBsp9J9Fdxzn0zSD6G+DM+LVHAM+b2ctE1VQ7lP0k+vsdcFq8rf2AKSlf74Y5DwquGZ1BNBdDsRuBD8Z/30Y0DeavzWxzvOwyorTVD0r6I/A9ku+UfwWMiKtd/hlYBIUZtv4FuBf4dbytl+LXfBaYFjfuPkzUQNyPmW2Ny7kzUSDIm5d/PXAR8OF4+S3AifmG5uCn0dd/AuPibX0ZeKionM5V5FlSnauSpO3N7NX4TuFnwOVmVhqcGiruVpuLq9H2Bv4XeHtRcHSuLG9TcK568yQdQ9TGcBuwoMHlSdIO3BlXkwn4tAcEl4bfKTjnnCvwNgXnnHMFHhScc84VeFBwzjlX4EHBOedcgQcF55xzBf8fKLHmpN3YAD4AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fac0a371048>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Draw the scatterplot of the vote_average and revenue\n",
    "plt.scatter(x=high_rev_df.vote_average, y=high_rev_df.revenue)\n",
    "plt.title('The correlation between Average Voting and Revenue')\n",
    "plt.xlabel('Average Voting')\n",
    "plt.ylabel('Revenue')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>vote_average</th>\n",
       "      <th>revenue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>vote_average</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.219513</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>revenue</th>\n",
       "      <td>0.219513</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              vote_average   revenue\n",
       "vote_average      1.000000  0.219513\n",
       "revenue           0.219513  1.000000"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate the correlation between 'vote_average' and 'revenue'\n",
    "high_rev_df[['vote_average', 'revenue']].corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It shows that the correlation between 'vote_average' and 'revenue' is 0.30. The correlation is relatively low. The third group is 'budget' and 'revenue'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEWCAYAAACJ0YulAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJztnXu8HWV197+/c7IhJ6KcYI4VDrkgtaEihkheRPG1gJdYKBDlptVavEC1WsVi2oSP5WL1NX1TrVXaIl6KKC8SLk2DYKMWvICiJiQhBkhFwyUnKOESQHIgJyfr/WNmdubsM7P37Mvs6/p+PifZe+aZmTXPnnnW86y1nvXIzHAcx3EcgL5WC+A4juO0D64UHMdxnCKuFBzHcZwirhQcx3GcIq4UHMdxnCKuFBzHcZwirhQagKSLJX2j1XLUS733IWmTpOMaKFJ03u9Lel+jz9utdGp9STpb0m2tlqPXcaWQAUm/i/3tkTQa+/6OVsvXCiRdIemT8W1mdriZfb9FIiXSCQ2kpPtjz9QTkm6SNLMN5GqbRlrSHEkWe+/ul7Sk1XJ1I64UMmBm+0V/wIPAybFtV7VavlIkTcmyzWkrTg6frwOB3wJfaLE87cpgWE+nA38n6Y2tFqjbcKXQOPaRdKWkp0MzyoJoh6SDJF0vabukLZI+nHYSSQOSPiPpAUlPSrpN0kC475Tw3DvCHvAfxo67X9LfSroLeEbSlJRt1chyraTfhHL8UNLh4fZzgXcAfxP22m6MyfCG8PO+kj4naVv49zlJ+4b7jpO0VdL5kh6R9LCkd1eo30Ml/SyU5T8lHRCT8xhJPw7rZUNkwpL0KeB/A5eGcl4q6RJJXwj3FyQ9I+n/xur+WUnTy5033Le/pK+Eso9I+qSk/nDf2eHv9o9hz3+LpD+ucH8AmNmzwHXAy2LXmjDaKe3BS3qjpHvDurkUUGxff/g8PRrK8aGwxz2l3H2Ez9ZlwKvDutuRJK+kd0u6J3zufy3pL2L7yv7Okl4oaZWkpyT9DDg0Sx2F9bQG2AQcGTtf4rMdbh8teWbmh3VSCL+/J7yPJyStljQ7VtYkvV/SL8P9/yJJ4b4JJlftHdGUrd+s99kSzMz/qvgD7gfeULLtYuBZ4ESgH/g0cEe4rw9YC1wI7AO8BPg1sDDl/P8CfB8YDs/1GmBf4A+AZ4A3AgXgb4D7gH1icq0HZgIDSdsqyRLexzdisrwHeH54/c8B62P7rgA+mVY3wCeAO4AXAUPAj4G/D/cdB+wOyxTCetsJTE+pk+8DI8DLgecB10dyhvX0WHiOvrB+HgOGYse+L3auE4CN4efXAL8CfhrbtyHjeVcCXwzleRHwM+Avwn1nA2PAOeFv+AFgG6BKzxQwDfgacGXJ/cfv4WzgtvDzDOApgp5zAfhoWLfvC/e/H7gbOBiYDnwPMGBKxvu4rcL7cBJBYy7gj8Lf8ZVZfmfgm8CK8NovD3/jxOsBc0rkPiY811uyvGfALcA5sfMtBy4LPy8ieJf+EJgCfBz4caysAd8CBoFZwHbgzSnvTKmcqfXbrn8tF6AmoeGrwCPALzKUnQ38N3BX+HIdXOe17ydZKXwv9v1lwGj4+VXAgyXllwL/nnDuPmAUmJew7++AFSVlR4DjYnK9J0HW98S+l5Wl9AEvKTcYPuz7h9+voLxS+BVwYmzfQuD+8PNx4X1Oie1/BDgm5drfB5aV1O8uggb3b4Gvl5RfDfx57Nh4gzpAoMBfCCwBLgC2AvsBlwCfD8ulnhf4PeA5QuUb7ns7cGv4+Wzgvti+aWHdvbjMM/U7YAdBI7oNOKLk/tOUwrsIOyDhd4X3EymFW4g1QsAbQlmmZLyPskoh4V5WAh+p9DuHv90YcFhs3/9Jux57G9sd4TkN+EdCRUvlZ/t9wC2xOnoIeF34/dvAe0verZ3A7PC7Aa+N7V8BLEl6Z2JyVqzfdv3rVDvzFcClwJUZyv4jQa/ra5JOIOjF/1kOMv0m9nknMDUcQs4GDioZfvcDP0o4xwxgKkGDWspBwAPRFzPbI+khgh5txEMJx8W3ZZYlHOJ+CjiDoKe/JybjkwnXKStv+Pmg2PfHzGx37PtOgoY5jfh9PEDQ85xBcE9nSDo5tr8A3Jp0EjMblbSGoFf7OoJ7PBI4NtwW2fLLnXd2+Pnh0IoAQUMSl7H4PJjZzrBcuftbZGbfC+v9VOAHkl5mZr8pcwwEdVq8rplZ+Fwk7mfy81DpPsoSmsUuIhjJ9hEowI2xImm/8xBBw1n6u1ZiBkGjex5BA1sg6CBUeravA74g6SDgpeE5on2zgX+W9Jn4rRG8W5FMpe93ud8you76bQUdqRTM7IeS5sS3STqUwPQyRPCjnWNm9xL0Kj8aFruVoCfTTB4CtpjZSzOUfZSgF3sosKFk3zbgiOhLaNOcSTBaiLCEc8a3VSPLnxI0Tm8g6MnuDzzBXnt10rVK5Z1NYPeFYNi9LcN104hH48wi6GU+SnBPXzezc1KOS5LzBwSmovnAz8PvC4GjgR+GZVLPK+lAgh7gjJIGr27MbBy4QdIXgdcSNGbPEDS2ES+OfX6YWN3Enov4/oNj3+P7HqL8fZT9jRX4iK4nGK38p5mNSVpJzKdRhu0Eo6KZwL3htlkZjovq6DOS3gL8JYFps+yzbWY7JH0HOJPATHS1hV338NhPWW1BI+V+m0r125Z0k6P5cuCvzOwo4GPAv4bbNwCnhZ/fAjxf0gubKNfPgKcUOHwHQifeyyX9r9KCZraHwDT22dA51i/p1eHLtwI4SdLrQ+fY+QQP3I/zkIXAl/AcgR19GsHQPs5vCey2aVwNfFzSkKQZBLbeeuZyvFPSyyRNI7BRXxc2Dt8ATpa0MLyfqaGDM2oIk+T8AUFDdreZ7SI0zxA0KtvDMqnnNbOHge8QNEwvkNQn6VBJf1TH/QFBoy7pVAL7/z3h5vXAWyVNk/T7wHtjh9wEHC7preHI9MNMbJhWAB+RNCxpkMAsBkCG+/gtcLCkfVLE3YfA37Qd2B2OGt6U5T4j5QdcHN7XywhMc9WwjCDYYSrZnu3/R/C7nxZ+jrgMWKq9gRT7SzojowzrgddJmiVpfwKTVXSPuT0nedIVSkHSfgROw2slrSdw7BwY7v4Y8EeS1hGYB0YIeihNIXz4TyYwUWwh6N1+maDnncTHCIbfPwceB/4B6DOzzcA7Ccwbj4bnPDls1PKQ5UqCofMIgaPyjpL9XwFepiAyJ2n09UlgDYEvZyNwZ7itVr5OYDb8DYGJ7cPhPT1EMKK5gKBxeghYzN5n+5+B08Ookc+H235M4FuIRgV3E4zQou9ZzvsugkbxboIR1HXsfeZq4UZJvyNwGn+KwCcSjbL+icBE8lsCJ3SxR2tmjxKY+JYRKPCXArfHzvslgobpLmAdcDPB8z+e4T5uIRjp/UbSo6UCm9nTBL/DivDYPwVWVXHPHyIww/yG4Lf99yqOhUAhPkFgFcjybK8iqJ/fmllxJG5m/0Hwnn1T0lPAL4Cs0WLfBa4hqN+1BA7pOI1+TnJHe0dQnUVoPvqWmb1c0guAzWZWtrJD5XGvmR1crpzjdCthb/4yM5vdalmc9qQrRgpm9hSwJRryhUPweeHnGZKi+1xKYJ5xnJ4gNKWcqGCOyjCBU/g/Wi2X0750pFKQdDXwE2Cugskx7yWYTPVeSRsIhrynhsWPAzZL+h+CELFPtUBkx2kVIgi1fYLAfHQPgX/HcRLpWPOR4ziO03g6cqTgOI7j5EPHzVOYMWOGzZkzp9ViOI7jdBRr16591MyGKpXrOKUwZ84c1qxZ02oxHMdxOgpJWWaMu/nIcRzH2YsrBcdxHKeIKwXHcRyniCsFx3Ecp4grBcdxHKdIx0UfOY6TjZXrRli+ejPbdoxy0OAAixfOZdH84coHOj2NKwXH6UJWrhth6Q0bGR0LkqGO7Bhl6Q3B2jeuGJxyuPnIcbqQ5as3FxVCxOjYOMtXb26RRE6n4ErBcbqQbTtGq9ruOBGuFBynCzlocKCq7Y4T4UrBcbqQxQvnMlDon7BtoNDP4oVzWySR0ym4o9lxupDImezRR061uFJwnC5l0fxhVwJO1bj5yHEcxyniSsFxHMcp4krBcRzHKeJKwXEcxyniSsFxHMcp4krBcRzHKeJKwXEcxyniSsFxHMcp4krBcRzHKeJKwXEcxyniSsFxHMcp4krBcRzHKZKbUpA0U9Ktku6RtEnSRxLKHCfpSUnrw78L85LHcRzHqUyeWVJ3A+eb2Z2Sng+slfRdM7u7pNyPzOxPcpTDcRzHyUhuIwUze9jM7gw/Pw3cA3geX8dxnDamKT4FSXOA+cBPE3a/WtIGSd+WdHjK8edKWiNpzfbt23OU1HEcp7fJXSlI2g+4HjjPzJ4q2X0nMNvM5gFfAFYmncPMLjezBWa2YGhoKF+BHcdxephclYKkAoFCuMrMbijdb2ZPmdnvws83AwVJM/KUyXEcx0knz+gjAV8B7jGzz6aUeXFYDklHh/I8lpdMjuM4TnnyjD46FvgzYKOk9eG2C4BZAGZ2GXA68AFJu4FR4G1mZjnK5DiO45QhN6VgZrcBqlDmUuDSvGRwHMdxqsNnNDuO4zhFXCk4juM4RVwpOI7jOEVcKTiO4zhFXCk4juM4RVwpOI7jOEVcKTiO4zhFXCk4juM4RVwpOI7jOEVcKTiO4zhFXCk4juM4RVwpOI7jOEVcKTiO4zhFXCk4juM4RVwpOI7jOEVcKTiO4zhFXCk4juM4RVwpOI7jOEVcKTiO4zhFXCk4juM4RVwpOI7jOEVcKTiO4zhFprRaAMfpBVauG2H56s1s2zHKQYMDLF44l0Xzh1stluNMwpWC4+TMynUjLL1hI6Nj4wCM7Bhl6Q0bAVwxOG2Hm48cJ2eWr95cVAgRo2PjLF+9uUUSOU46rhQcJ2e27RitarvjtBJXCo6TMwcNDlS13XFaSW5KQdJMSbdKukfSJkkfSSgjSZ+XdJ+kuyS9Mi95HKdVLF44l4FC/4RtA4V+Fi+c2yKJHCedPB3Nu4HzzexOSc8H1kr6rpndHSvzx8BLw79XAf8W/u84XUPkTPboI6cTyE0pmNnDwMPh56cl3QMMA3GlcCpwpZkZcIekQUkHhsc6TtewaP6wKwGnI2iKT0HSHGA+8NOSXcPAQ7HvW8NtpcefK2mNpDXbt2/PS0zHcZyeJ3elIGk/4HrgPDN7qnR3wiE2aYPZ5Wa2wMwWDA0N5SGm4ziOQ85KQVKBQCFcZWY3JBTZCsyMfT8Y2JanTI7jOE46eUYfCfgKcI+ZfTal2CrgXWEU0jHAk+5PcBzHaR15Rh8dC/wZsFHS+nDbBcAsADO7DLgZOBG4D9gJvDtHeRzHcZwK5Bl9dBvJPoN4GQM+mJcMjuM4TnX4jGbHcRyniCsFx3Ecp4inznacJuDrKTidgisFx8kZX0/B6STcfOQ4OePrKTidhCsFx8kZX0/B6SRcKThOzvh6Ck4n4UrBcXLG11NwOgl3NDtOzvh6Ck4n4UrBcZqAr6fgdApuPnIcx3GKuFJwHMdxirhScBzHcYq4UnAcx3GKuFJwHMdxirhScBzHcYq4UnAcx3GKuFJwHMdximRWCpJmS3pD+HlA0vPzE8txHMdpBZmUgqRzgOuAL4abDgZW5iWU4ziO0xqyjhQ+CBwLPAVgZr8EXpSXUI7jOE5ryKoUnjOzXdEXSVMAy0ckx3Ecp1VkVQo/kHQBMCDpjcC1wI35ieU4juO0gqxKYQmwHdgI/AVwM/DxvIRyHMdxWkOm1Nlmtgf4UvjnOI7jdCmZlIKkLST4EMzsJQ2XyHEcx2kZWRfZWRD7PBU4Azig8eI4Tm2sXDfS1Subdfv9Oe1DVvPRYyWbPifpNuDCtGMkfRX4E+ARM3t5wv7jgP8EtoSbbjCzT2SRx3HirFw3wtIbNjI6Ng7AyI5Rlt6wEaBpDWeejXY73J/TO2SdvPbK2N8CSe8HKs1ovgJ4c4UyPzKzI8M/VwhOTSxfvbnYYEaMjo2zfPXmplw/arRHdoxi7G20V64bacj5W31/Tm+R1Xz0mdjn3cD9wJnlDjCzH0qaU5NUjlMF23aMVrW90ZRrtBvRk2/1/Tm9RVbz0fE5Xf/VkjYA24CPmdmmpEKSzgXOBZg1a1ZOojidykGDA4wkNJAHDQ405fp5N9qtvj+nt8hqPtpX0p9KukDShdFfnde+E5htZvOAL1Aml5KZXW5mC8xswdDQUJ2XdbqNxQvnMlDon7BtoNDP4oVzm3L9tMa5UY12q+/P6S2yTl77T+BUAtPRM7G/mjGzp8zsd+Hnm4GCpBn1nNPpTRbNH+bTbz2C4cEBBAwPDvDptx7RNCds3o12q+/P6S2y+hQONrNKTuOqkPRi4LdmZpKOJlBQpVFOjpOJRfOHW9ZIRtfNM2S0lffn9BZZlcKPJR1hZhuznljS1cBxwAxJW4GLgAKAmV0GnA58QNJuYBR4m5l5kj2nI/FGuzw+z6JzyKoUXgucHc5sfg4QYGb2irQDzOzt5U5oZpcCl2YV1HGczsTnWXQWWZXCH+cqheM4XUveIbtOY8nkaDazB4CZwAnh551Zj3Ucp7fxeRadRdaQ1IuAvwWWhpsKwDfyEspxnO4h75Bdp7Fk7e2/BTiFMAzVzLZROc2F46Syct0Ixy67hUOW3MSxy25pWEoIp/3weRadRVafwq4wdNQAJD0vR5mcLscdj71FM0J2ncaRVSmskPRFYFDSOcB78AV3nBpxx2Pv4SG7nUPW3Ef/GK7N/BQwF7jQzL6bq2RO1+KOR8dpX7KuvPZR4FpXBE4jyCPBm0+OcpzGkNXR/AJgtaQfSfqgpN/LUyinu2m04zHv9Qwcp5fIOk/hEjM7HPggcBDwA0nfy1Uyp2tpdII3X4TGcRpHVkdzxCPAbwgS172o8eI4vUIjHY/uo3CcxpF18toHJH0f+G9gBnBOubxHjtNMfHKU4zSOrCOF2cB5ZrY+T2EcpxYWL5w7Yd4DtN/kKHeEO51CVp/CEmA/Se8GkDQk6ZBcJXOcjLT7IjTuCHc6iawhqRcBCwjmKPw7e3MfHZufaI6TnXaeHOWT9ZxOwnMfOU7OuCPc6SQ891EX4vbr9iKPyXqOkxdZRwqluY++B3w5P7GcWnH7dfvhWUKdTsJzH3UZjbBf+0ijfkrr8LSjhrn13u1ep07bk3nyWqgEvgsgqV/SO8zsqtwka0M6obGs137taa3rJ6kOr/nZQ+w3tdq5oo7TfMqajyS9QNJSSZdKepMCPgT8GjizOSK2B51ilql3IpenjKifpDoc22M8sXOsrZ8dx4HKPoWvE5iLNgLvA74DnAGcaman5ixbW9EpjWW99muPlKmfLHXVbs+Or4TnRFQaz77EzI4AkPRl4FFglpk9nbtkbUanNJb1rnLlkTL1k1aHpbTLs+MmQydOJaUwFn0ws3FJW3pRIUBnNZb1TOTqhJQR7U5SHSYxUMga/JcvPrnOiVPpqZwn6anw72ngFdFnSU81Q8B2oVfCCts9ZUQnUFqHaYzu3tM0mcrRKaNgpzmUHSmYWX+5/b1ELy0+3s4pIzqFeB3OWXJTYhmzZkqUTieNgnuVZkY+eoxcFXhj6dRCn2BPggLoKzeMaCKLF85l8bUbGIsJWehT142CO5Vm+3xyM2pK+qqkRyT9ImW/JH1e0n2S7pL0yrxkcZxGU020zr5Tkl+ztO0toVRBtYnCcpof+ZjnU3kF8OYy+/8YeGn4dy7wbznK4jgNo9o5K8+OJfsO0rY3m+WrNzM2PnEoMzZubRUy28s02+eTm/nIzH4oaU6ZIqcCV5qZAXdIGpR0oJk9nJdMvUS7z75ud/nKUW20Trvb7N3R3N40+/lp5fh1GHgo9n1ruG0Sks6VtEbSmu3btzdFuE6m3Wdft7t8lai2EW33yLVOWM60lyfXNfv5aaVSSLJaJsZjmNnlZrbAzBYMDQ3lLFbn0+6zr/OQr5mNRrWNaLuH+U7bJ7kZSNvebDq9E1EvzX5+Whl9tBWYGft+MLCtRbJ0FWk91pEdoxy77JammGrKmYcaba5odnRGLRP82jly7ZePPFPV9mbjk+ua+/y0siuwCnhXGIV0DPCk+xMqk6VHXG7Y34xeVqWeXaPNFc0eGbV7z7/bcJ9Hc8ltpCDpauA4YIakrcBFBGs7Y2aXATcDJwL3ATuBd+clS7eQtUdcKc1C3r2sSj27RqfSSMszlCX/UK20c8+/22h3R323kWf00dsr7Dfgg3ldvxvJOoyOz75OaxhLe1mNjAaq1LNr9Ozwdp8c1sm0Q5SY5+NqLj6juYOoZhgd9WSPXXZLxV5W0gjkvGvW89cr1rPHAvPI8YcNZV45LEvPrpE97SSFUG67M7Gx75cYT8i5MThQaIvsqb2UYqYdcKXQQdQyjM7Sy0oagcDeRnVkxyjfuOPB4vZKjUM39OzaoYecF6WdgCSFMFDoR6JtHLxurmse7RFz5mSilnjlLE7RWhx2aY7cqDEdHRunX4H9Josjtp6Q0sGBQlXbK9HtIZBpnYB+acIzsmPn2OSDcQdvt+MjhQ6i1mF0pV5W1kVhSknyS5T2QONK69hltyTKXW9I6cWnHF40dUX0Kdgely1rvXV7CGRao77HjC3LTip+T/NJuYO3u3Gl0GFkGUZXa/rIuihMKaWNQ1pjesmNm3h2bE9qo1+pEc5yP/0Se2JmkGiUAtUrnW4PgcxqhuwGM6BTPW4+6jJqMX1EJqZqzC1JjUNao/nEzrGy8wjKNcJZ7mf56s0T0j4DjO3Zm9Ct2nkMnZD2oR6ymiF9PkZv4iOFkGY6FvO8Vq2mj2gE8vGVG7nqjgcn5BsR8JpDD+D+x0bLylytGSpSBuV6rlnup1LPvtp5DFl6yNX+hu3kuK7GDOkO3t7DlQLBC7v4ug3F9MEjO0ZZfN0GoPGhd3mnZKjX9PHJRUewYPYBNTVgaY3pvlP62DE62WkZ9byPP2xoQnRTxPGHDXFVwvbS+6lkDpGSVzmLWZgmNdqnHTWcGoJb7W/YzOcrK97YO2m4UgAuuXFTYj75S27c1PAXJ28nZiNmf9baYKT1QIFJyqLQJ3bu2s0hS26iT8mzzG69d3um+6nUs09b9jLantTIX792ZIKpJIqO2rZjlL6EuP5yv2Ezny/HqRdXCgQ272q210PeTsxWOwfLKZRIWew/UODp53YX6zcpTh6COvmns45MvJ/jDxuaEM1UrmdfjkgplWvkV64bmbBcZTl5k6jl+Wq2uamdzFtOa3Gl0GTyzuPSrrM/48pi/ie+w3iG6cYHDQ4k3s/xhw1x/dqRCT37a372EPtNTX6cBwcKieYrCHK1pzXyIztGOWTJTcVyWeRtBM3O+trs6zntjSsF0huNWic/laMZPflm2Ivr6VlmGYHF66T0fo5ddsskE9zYHiuet7RRu/iUwyctTJ+VrEeU+w2Vcp601EzNnifR7fMynOrwkFSCSU6FkuxphT5NmPzUKJLC/E47KojV75RVpZLCRBdft4EjL/lO3feQJfQxi6ktHnK6aP4wy8+YV6zzRpJF3jTFkra92fMkun1ehlMdPlKg+SaXeM+33qF7Uo8973tJ6lmOjVtxtFXpHsqNzNZf9KaK188a+hovE6/ztCSB1TJ9WoF1F1aWd/q0QuLoaPq05JFos1NFe2pqJ46PFEIWzR/m9iUnsGXZSdy+5ISGNqLl8vqkDd3PX7GhYq87scd+7QYWX7ch17w91fbUS6l3ZHb8YdmWZO1PiWpKmrxVLYV+cdHJ2eStFP1USrPX5G33NaSd5uIjhZypNBJIa2Aj52e5Xndijz3Bbh4pmY9es74hI4esPfW0e6t3ZHbrvdszlUtzIJdeP4vfoNAn9ps6hR07x6qW98kUJ3fa9iz108hooXYNTnBagyuFnKnkxMvSwKY5/aqx+WZRMlnJmiupdM2G0kbn9iUnZL5m/Piszt9yk9Pio41yi/SYUXcjWYt5plywQB7RQj6ZzYlwpZAzlZx4WRvYpPPUmt00Tclk7X2W9iwHpxX43bO7J4xS4uaHLI1YuWuXHp+VcpPT4jOokwYUhX6x/PR5DWkoGx1x5tFCTp64UsiZSr3E0gY2aSJVvHycpMam0CcQk2bQllIp7XWl3mdpz7Jco17Ob/LRa9ZPUipZsqhWQ9bjo0yrjTafLJo/zJoHHufqnz7EuBn9EqcdVXvP3KOFnDxxpdAAyjWIWXqJUQO7ct0IF6/aNCkyJ61XWS6tRLVKpt7eZznzQyW/SVJkTvzatTZ2+/Sr7PWT5Lk/tp5Ao1i5boTr144U73fcjOvXjrBg9gE1KYbBlGimwZRoJsepBlcKdVKph53ViZdmIpk+rcBFJx+e2nikNcblTC9JSibNDFWpQc1ictq/zIzickQy1Womi0ZLWY9Pi1aql0abe6qNZmoEngajd3ClUCdZXvgsTrw0E8e0fabU9fJljWRJm3VbzhmapBDPu2Y9l9y4aYIiq6etnbPkJqZPK6Q6g8sRFc/qt0mLVqqXRpt7qo1mqhdPg9FbuFKok7QXeyRcICYyC1XqZeVpJ66klJav3pyahqGcMzRNkT2xc4zzr93Axas28eToWOZooTTqTUyY1W8znNNkrbSR0v41plFp9mQzd2z3Fq4U6qScaWLpDRtZ88Djk5K3JUXeVONgbjRpisco3xMsp7DG91hNJqO8KDeLHPKdrJU2Utq1ezx13epyNDsTrju2ewtXChWo1MsvZ5oYHRsvRpyUbo+nZV56w8ZEhRC96JVkSIrBryaNdJpi65c4ZMlNDVtprV1oxGStamzsaSOdnWN72Llj7+pwWU0yzZ5s5mkwegtZnt6pHFiwYIGtWbOmKddK61GWJj9buW6E865ZX9W5BWxZdlJqHp5+ic+cOQ+YvEBNXIYsMfyFPrH8jPSY+9KVwdLOUTqjN0m2Sij8p1GPXbnzxXMT1esojR+//0CBZ3btnlBfSc9FxKFLb87srxgeHKhqUl8zyPoeOO2NpLVmtqBSOc99VIY0W+p516yfkJNo0fzhVHt0WkRL1MtKG4LvMUuN0Y/nFcoSgz+2x/joNevL51Kq0GZFqanj+ZQAPv3WIzJnHh0eHGDLspMaGiWzZdlJ/NOZR1LoL8mlFMuHK/mtAAATVklEQVRNlJQjqpp8UKXH7xgdm6RAy+V6qsaB3Y4mmaTMvq4QupdczUeS3gz8M9APfNnMlpXsPxtYDkRv56Vm9uU8ZaqGci9o1LCseeBxbr13OyM7RidF8AwU+jntqOEJPoVoe9TTrjQ0r2TPzdqIRHIlmSmWr95c9VoD0eSzz5w5j38668iK6xXkYfOOFHElc0qlyXOVTHJp/p5S0n6L/ozHQ/uaZDwNRu+Qm1KQ1A/8C/BGYCvwc0mrzOzukqLXmNmH8pKjHirZzEfHxrnqjgeLDa6xd0GV4VhDs2D2ATVPbqukNGqx65dGjtTaOx03Y+kNG/n0W4/grKNnTpixe8xLpnP/Y6OJ91xuJbSspE0ATCJL0sHF127gkhs3sWPn2CTzUL0NetbjPTOp0w7kOVI4GrjPzH4NIOmbwKlAqVJoGWl25mh7lsa29HWPFEI1duGphb6iUhgcKHDxKXtj/I8/bGhCnp6IkR2jHLvsFua8sDZnb/yY4Pp7qj4HBArm4lWbeGbX7gkzdn92/xOpuYP+ZN6BifdUjkpZSsv5DLIozvjKbbUorEKf2Llrd6JjPm2koFA2nxDmtBN5KoVh4KHY963AqxLKnSbpdcD/AB81s4dKC0g6FzgXYNasWQ0RLm1CTmkIaS1EDXZSsri4+QYmO2qf2z2xcb7profLXqceG3TUgD1bQSEImNKvVEd0UiM6Nm5ccuOmxIR3fRlms/UJXjC1wJOjgRKY88IB7vj1ExjwmyefZc0Dj2deqCjr5LVqiCupaGSRthxo2kjBoO2cyo6Tp6M56c0vfTtuBOaY2SuA7wFfSzqRmV1uZgvMbMHQULYFViqRZme+6o4H6248BEWn5BM7xybZ2iPzTSUnMlSeuFWPzzZyumY5x/LT51U9MzmSvdRRm8Wc0h8uurNl2Ukcf9gQt//q8QkjkW/c8SAfXxk0vJUWKlq+ejOnHTVc93Kc/VLR0br8jHmsu/BNbFl2Es/bd0pZx3NaEEJek+Ucpx7yVApbgZmx7wcD2+IFzOwxM3su/Pol4Kgc5ZlAuQlb9ZCWLiLp+p0yKahP4rxr1tccNVRLltOxcSs2qlf9NNnUFG1PMw2NmxUV3/VrR1i8cC5bakx4N1Do5zNnzktcma/S75i2UlzWFeQcp5nkqRR+DrxU0iGS9gHeBqyKF5B0YOzrKcA9OcozgTyiPIYHBzIrlYMGB1JliG8frDEVQiOpNSdQJHutSi46rlICuCwjmCw99ziFPjF9WqE4MjjtqCA8OCmst9LvmLZSXNYV5JIot8Sr49RDbkrBzHYDHwJWEzT2K8xsk6RPSDolLPZhSZskbQA+DJydlzyl5BHlcfuSEzI14lGUSZa1cbOuW9xKpk8rlF1zOS2ls4KlHyrO5SjHIUtuyjyCiUYUSfVeKsHRh0wvmocWL5zL9WtHUuc5VPodGz0irHfeheOUI9fJa2Z2s5n9gZkdamafCrddaGarws9LzexwM5tnZseb2b15yhNn0fxhpjcw/3zUsFXqtcYn/iyaP8xpRw0Xj01afGXR/GGet099i8znyUChn4tOPpyzjp454T6OPmR6sWe9I8Uvsv/UAluWncTbXzUzcX8W80o1Y5hIvtLJWM/bp3/SeW7/1eP84d99m0OW3MT5KzaU9f1UmtyVZURYDVl8Uc3GRy7dQ0/mPooiYZ7YOZbZB1CJyMSS1gDC3t7jmgce5/wVGyaZZZIWX1m5boRdu2sLF83C8OAAO2ORM9UgghnNwKRFZG7/1eMVj49SPX9rQ3KE1TfueJCr7ngQNSgtRry+4/MaDl16c2L5KEw3zXwW7+mXmyexeOHcSWlECv2qebTabr4oT63dXfScUih9gEsnnD3+zHM1xeyLwJRRbvZrlCKjHFGZ81ds4O2vmsm3Njxc9WzjaqgnoZ0B512zvqoZu3H6JOYsuaniNRqitUn3JdTqM6kq9XXShJYaabcEdZ5au7voudxHSQ9wfMLZeI0NsIV/jVqoJQq7bKf002nUes95LWqTRHxyWal5o9YV17IelpRGZGyP1WzuyeKLaibtNnJx6qPnlEKlB3hXhQXvnc5ChFFQYlJCv0gxpPk0KlHOVBin0Y1muyWoa7TPxGktPacU0ob8+w8UOs451uuTn6LJZOXIMrnsk4uO4J3HzNobLJDx+lkbvXLPXK0smj/M7UtOSJw30WzabeTi1EfP+RTShvxPPTvG4murWxOh1ezYuSv3awwU+uua4d0oR34p8TQTlSi3ZGo8V9EnFwVO87Q1LuJU0+jt2p1cf9H2etd6aDXNXvTHyZeeUwppjcgeq35h+FbzzK7G5fJJ47SjhqtOXpcXfQp+IynwR2SNmEpbIxmYYE6CoIGrpBCGq2z0dqYELuwc29MxkTuVFJen1u4eek4pdOoSkq2inlm30NhRQqS0zao7bzUznhfNH06NpuqX+NWnT6ziypXphMidTlFcTmPoCaUQ7+UMFHrOjVIX3RBBUq1DOC0qqtZoqenTComjmunTCh0RudMJistpHF3fQq5cN8Jfr1hfTAmQNpR3ksnbolZP1tKsZHUIR+XSUpXUmofqopMPT10uNE22tNQgraATFJfTOLpeKVxww10d5yvoJfL8aaJmOCk6ppS44zjN3FTjdIZgre3T500IIY0WIFq8cO4khQHw5M6xtomG85DT3qLrlYKPDHqXyFSYFNf/zmNmTfgez4Ka5sDOaoaqhkXzh5nSN1kp7AEuXrWp4derBQ857S16wqfg9CbxDkG56JhSR2oa5XrGpdE5xx82xK33bq+4+t6i+cOpaVXaZTa7h5z2Fq4UnI5loNDHs2N76jZBZVkEqFwCu6TonHgYb9LIo9MctR5y2ju4UnA6lgOety+3LzmhYlI92NuTH9kxWgw5jeYbZAlRHi+T/qSWleVgr6O2XHSS4zSbrvcpOPly/7KTmhJBlESW6JdDltzE/E98pxiBBntDSyMzThYHcjkbf61ROJE5qlx0kuM0G1cKTt1MbdHcj6hRTQjeKWIE5pu0CLTRsfHMazWk2fhricKJO2rLRSc5TrNx85FTF1lMN3kQb1RbHV+2eOHcio7qQr943j5TeHJ0zNNEOG2NKwWnoxBMalTrXZZhcKDAc7v3VPQLJESOAsnROfHoI4/WcToJVwpOx9AvsafBC/MMFPq5+JTAdh816mlXKDcJ0nv6TrfgSsHpGEodxFBfQrbBgQIXn3J48RzR/2mps3tp/YpOT+ft1I47mp2W0Kcg5LLWyKX4IjlpjXW0CE/SDObPnXUk6y96U2JD1+szeKN5F1G+sNKV6pzuxpWC0xL2GEzbZwpblp1U8xrJUSjo8YcNTVIuA4V+PnPmvOLKZAtmH5D5vO223GWzKZcV1el+3HzktIyoUT/mJdO5/VePV338QYMDrFw3wvVrRyb4AUSwOFDUiNeyHkAv+wg8K2pv4yMFp2VE6aHvfvjpqo+NzDlJvVoDbrrr4eJ37/lWh2dF7W1cKTgtIwokyrqsZkQ8q2laioonYqmnvedbHb3uU+l1clUKkt4sabOk+yQtSdi/r6Rrwv0/lTQnT3mcxhM5eWvxCjxZZRbQQp/43FlHsnjhXK5fO1IxZ1E0EvCeb3X0uk+l18nNpyCpH/gX4I3AVuDnklaZ2d2xYu8FnjCz35f0NuAfgLPykslpPLcvOQEonzq6L2XN4/hKZ0kpJMTeRXji4aPHLrslUwK6aCSQNOPYe77l6WWfSq+Tp6P5aOA+M/s1gKRvAqcCcaVwKnBx+Pk64FJJMmvwDCWnLuKNc5x4KGi16xXEG+WLTzmcxdduKK43AMGoYPkZyfl/spp9IqXj6wE4TnbyVArDwEOx71uBV6WVMbPdkp4EXgg8mqNcDoHd8LNnHTkhQidqNAenFTCjmKfn+MOGuH7tSM097UqNcrWN9kGDAxVNR6Xyec/XcbKRp1JIMjOXdjizlEHSucC5ALNmzapfsh7npS96Ht/96+MmbKvUaC6YfUBdPe1K56+m0U4yB1VKOOc4TjbyVApbgZmx7wcD21LKbJU0BdgfmBSwbmaXA5cDLFiwoCrT0v3LTmpZJs80pvaLez91YvH7Gz/7fX75yDPF730EmnH/gQK7do9PWmc6WnFsasnKY4U+2G9qsGBL6UIy9TaQ7dTTdnOQ4+SH8jLfh438/wCvB0aAnwN/amabYmU+CBxhZu8PHc1vNbMzy513wYIFtmbNmlxkdhzH6VYkrTWzBZXK5TZSCH0EHwJWA/3AV81sk6RPAGvMbBXwFeDrku4jGCG8LS95HMdxnMrkmubCzG4Gbi7ZdmHs87PAGXnK4DiO42THZzQ7juM4RVwpOI7jOEVcKTiO4zhFcos+ygtJ24EHajx8Bu09Ma7d5YP2l9Hlqw+Xrz7aWb7ZZjZUqVDHKYV6kLQmS0hWq2h3+aD9ZXT56sPlq492ly8Lbj5yHMdxirhScBzHcYr0mlK4vNUCVKDd5YP2l9Hlqw+Xrz7aXb6K9JRPwXEcxylPr40UHMdxnDK4UnAcx3GKdKVSaPe1oTPId7ak7ZLWh3/va7J8X5X0iKRfpOyXpM+H8t8l6ZVtJt9xkp6M1d+FSeVykm2mpFsl3SNpk6SPJJRpWf1llK9l9Rdef6qkn0naEMp4SUKZlr3DGeVr6TtcF2bWVX8EGVl/BbwE2AfYALyspMxfApeFn98GXNNm8p0NXNrCOnwd8ErgFyn7TwS+TbBI0jHAT9tMvuOAb7Wo7g4EXhl+fj5B+vjS37dl9ZdRvpbVX3h9AfuFnwvAT4FjSsq08h3OIl9L3+F6/rpxpFBcG9rMdgHR2tBxTgW+Fn6+Dni9pKRV4FolX0sxsx+SsNhRjFOBKy3gDmBQ0oHNkS6TfC3DzB42szvDz08D9xAsOxunZfWXUb6WEtbL78KvhfCvNCKmZe9wRvk6lm5UCklrQ5c+9BPWhgaitaGbQRb5AE4LTQvXSZqZsL+VZL2HVvLqcHj/bUmHt0KA0KQxn6AnGact6q+MfNDi+pPUL2k98AjwXTNLrcMWvMNZ5IP2fodT6Ual0LC1oXMiy7VvBOaY2SuA77G3R9QutLL+snAnQZ6XecAXgJXNFkDSfsD1wHlm9lTp7oRDmlp/FeRref2Z2biZHUmwjO/Rkl5eUqSldZhBvnZ/h1PpRqVQzdrQ0bKhiWtD50RF+czsMTN7Lvz6JeCoJsmWlSx13DLM7KloeG/BQk8FSTOadX1JBYIG9yozuyGhSEvrr5J8ra6/Ell2AN8H3lyyq5XvcJE0+TrgHU6lG5XCz4GXSjpE0j4ETqhVJWVWAX8efj4duMVC71A7yFdiXz6FwO7bTqwC3hVG0RwDPGlmD7daqAhJL47sy5KOJnjOH2vStUWwzOw9ZvbZlGItq78s8rWy/sJrDkkaDD8PAG8A7i0p1rJ3OIt8HfAOp5LrcpytwNp8beiM8n1Y0inA7lC+s5slH4CkqwkiUGZI2gpcROBMw8wuI1hi9UTgPmAn8O42k+904AOSdgOjwNuaqPSPBf4M2BjanAEuAGbF5Gtl/WWRr5X1B0GE1Nck9RMopBVm9q12eYczytfSd7gePM2F4ziOU6QbzUeO4zhOjbhScBzHcYq4UnAcx3GKuFJwHMdxirhScBzHaWNUIQFkSdlZYcLDdeFs6hOrvZ4rBccJkTQeZrTcIOlOSa+p8vjjJH2rjutfUOuxTldzBZMn76XxcYIQ2fkEYbr/Wu3FXCk4zl5GzezIML3DUuDTTb6+KwVnEkkJICUdKum/JK2V9CNJh0XFgReEn/enhpnyrhQcJ5kXAE/A5BGApEslnR1+frOkeyXdBrw1VmZI0nfDEccXJT0QpYqQ9E4F+fjXh/v6JS0DBsJtVzXzRp2O5HLgr8zsKOBj7B0RXAy8M5zUeTPwV9We2JWC4+wlapTvBb4M/H25wpKmEuS1ORn438CLY7svIki98ErgPwhnDEv6Q+As4Ngwodo48A4zW8Lekco7GnxfThcRJjN8DXBtOCv9iwSzrAHeDlxhZgcTzJr/uqSq2vmuS3PhOHUwGjbUSHo1cGVC9ss4hwFbzOyX4THfAM4N970WeAuAmf2XpCfC7a8nSI728zC90ABB+mXHyUofsCN6Vkt4L6H/wcx+EnZcZlDFM+YjBcdJwMx+QvAyDRHkr4m/K1PjRVNOkbbgi4CvhSOCI81srpldXK+8Tu8QpjrfIukMKC7vOi/c/SBBxyMalU4FtldzflcKjpNA6LjrJ8gO+gDwMgXrAu9P+NIRZMY8RNKh4fe3x05xG3BmeK43AdPD7f8NnC7pReG+AyTNDveNKUhr7ThFwgSQPwHmStoq6b3AO4D3StoAbGLv6o3nA+eE268Gzq42maGbjxxnLwOxzKEC/tzMxoGHJK0A7gJ+CawDMLNnJZ0L3CTpUQJFEJmbLgGulnQW8APgYeBpM3tU0seB74S23jHggwSK53LgLkl3ul/BiTCzt6fsmhSmamZ3E2TCrRnPkuo4OSBpX2A8TJX+auDfUmzAjtNW+EjBcfJhFrAiHA3sAs5psTyOkwkfKTiO4zhF3NHsOI7jFHGl4DiO4xRxpeA4juMUcaXgOI7jFHGl4DiO4xT5//LTKtfamC01AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fac0a2f21d0>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Draw the scatterplot of the budget and revenue\n",
    "plt.scatter(x=high_rev_df.budget, y=high_rev_df.revenue)\n",
    "plt.title('The correlation between Budget and Revenue')\n",
    "plt.xlabel('Budget')\n",
    "plt.ylabel('Revenue')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>budget</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.660688</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>revenue</th>\n",
       "      <td>0.660688</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           budget   revenue\n",
       "budget   1.000000  0.660688\n",
       "revenue  0.660688  1.000000"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate the correlation between 'vote_average' and 'revenue'\n",
    "high_rev_df[['budget', 'revenue']].corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "The correlation of 0.56 is relatively high for these two variables.\n",
    "\n",
    "Overall, for the high revenue group, the revenue is related to the 'popularity' and 'budget', and less related to 'vote_average'."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Research Question 2: Which genres are most popular from year to year?\n",
    "In order to answer the question, the first thing we need to do is to calculate the most popular one in each year. First, we need to extract the relevant data points according to this question."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>release_year</th>\n",
       "      <th>genres</th>\n",
       "      <th>popularity</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2015</td>\n",
       "      <td>Action|Adventure|Science Fiction|Thriller</td>\n",
       "      <td>32.985763</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2015</td>\n",
       "      <td>Action|Adventure|Science Fiction|Thriller</td>\n",
       "      <td>28.419936</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2015</td>\n",
       "      <td>Adventure|Science Fiction|Thriller</td>\n",
       "      <td>13.112507</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2015</td>\n",
       "      <td>Action|Adventure|Science Fiction|Fantasy</td>\n",
       "      <td>11.173104</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2015</td>\n",
       "      <td>Action|Crime|Thriller</td>\n",
       "      <td>9.335014</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   release_year                                     genres  popularity\n",
       "0          2015  Action|Adventure|Science Fiction|Thriller   32.985763\n",
       "1          2015  Action|Adventure|Science Fiction|Thriller   28.419936\n",
       "2          2015         Adventure|Science Fiction|Thriller   13.112507\n",
       "3          2015   Action|Adventure|Science Fiction|Fantasy   11.173104\n",
       "4          2015                      Action|Crime|Thriller    9.335014"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie_data_genres = movie_data[['release_year', 'genres', 'popularity']]\n",
    "movie_data_genres.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Then, we need to split the row with more than one genre into different rows. The code below is sourced from https://stackoverflow.com/questions/50731229/split-cell-into-multiple-rows-in-pandas-dataframe."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>release_year</th>\n",
       "      <th>genres</th>\n",
       "      <th>popularity</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2015</td>\n",
       "      <td>Action</td>\n",
       "      <td>32.985763</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2015</td>\n",
       "      <td>Adventure</td>\n",
       "      <td>32.985763</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2015</td>\n",
       "      <td>Science Fiction</td>\n",
       "      <td>32.985763</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2015</td>\n",
       "      <td>Thriller</td>\n",
       "      <td>32.985763</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2015</td>\n",
       "      <td>Action</td>\n",
       "      <td>28.419936</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   release_year           genres  popularity\n",
       "0          2015           Action   32.985763\n",
       "0          2015        Adventure   32.985763\n",
       "0          2015  Science Fiction   32.985763\n",
       "0          2015         Thriller   32.985763\n",
       "1          2015           Action   28.419936"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Split the row with more than one genre into different rows\n",
    "\n",
    "from itertools import chain\n",
    "\n",
    "# Return list from series of '|'-separated strings\n",
    "def chainer(s):\n",
    "    return list(chain.from_iterable(s.str.split('|')))\n",
    "\n",
    "# Calculate lengths of splits\n",
    "lens = movie_data_genres['genres'].str.split('|').map(len)\n",
    "\n",
    "# Create new dataframe, repeating or chaining as appropriate\n",
    "movie_data_genres = pd.DataFrame({'release_year': np.repeat(movie_data_genres['release_year'], lens),                       \n",
    "                          'genres': chainer(movie_data_genres['genres']),\n",
    "                          'popularity': np.repeat(movie_data_genres['popularity'], lens)})\n",
    "\n",
    "movie_data_genres.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "After splitting, we need to select the most popular genres for each year. The code below is sourced from https://stackoverflow.com/questions/31361599/with-pandas-in-python-select-the-highest-value-row-for-each-group."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>release_year</th>\n",
       "      <th>genres</th>\n",
       "      <th>popularity</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1960</td>\n",
       "      <td>Thriller</td>\n",
       "      <td>0.811910</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1961</td>\n",
       "      <td>Animation</td>\n",
       "      <td>2.631987</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1962</td>\n",
       "      <td>Adventure</td>\n",
       "      <td>0.942513</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1963</td>\n",
       "      <td>Animation</td>\n",
       "      <td>2.180410</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1964</td>\n",
       "      <td>War</td>\n",
       "      <td>0.930959</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   release_year     genres  popularity\n",
       "0          1960   Thriller    0.811910\n",
       "1          1961  Animation    2.631987\n",
       "2          1962  Adventure    0.942513\n",
       "3          1963  Animation    2.180410\n",
       "4          1964        War    0.930959"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# A function is defined for the selection\n",
    "def func(group):\n",
    "    return group.loc[group['popularity'] == group['popularity'].max()]\n",
    "\n",
    "#Calculate the mean popularity for each genre in each year\n",
    "movie_data_pop = movie_data_genres.groupby(['release_year', 'genres'], as_index=False).mean()\n",
    "\n",
    "# Select the most popular genre for each year\n",
    "movie_data_most_pop = movie_data_pop.groupby('release_year', as_index=False).apply(func).reset_index(drop=True)\n",
    "movie_data_most_pop.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Then, a scatterplot is drawn to show the change of the most popular genre over the year."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fac0a2cbeb8>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Draw the scatterplot to show the change of the most popular genre\n",
    "plt.scatter(movie_data_most_pop.release_year, movie_data_most_pop.genres)\n",
    "plt.title('The change of the most popular genre over the year')\n",
    "plt.xlabel('Year')\n",
    "plt.ylabel('Genre')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the scatterplot above, it is easy to show that the most popular genre changed over the year. However, in some periods there are no or little changes. Overall, the most popular genre in 1990s is animation, while it becomes fantasy in 2000s.\n",
    "\n",
    "Next, in order to show the percentage of each genre, a pie chart is drawn sourced from https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fac0a265ac8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Draw the pie chart of genres\n",
    "sizes = movie_data_most_pop.genres.value_counts().values\n",
    "labels = movie_data_most_pop.genres.value_counts().index\n",
    "\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.pie(sizes, labels=labels, autopct='%1.1f%%')\n",
    "ax1.axis('equal')\n",
    "plt.title('The percentage of each genre')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the pie chart, the 'Animation', 'Adventure', and 'Fantasy' account for a majority of percentage over the year, while other genres like 'Thriller' and 'History' are less frequent to become the most popular genre."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# <a id='conclusions'></a>\n",
    "## Conclusions\n",
    "\n",
    "Conclusions\n",
    "Based on all of the discovery above, some conclusions are drawn:\n",
    "\n",
    "**The revenue changed drastically over the year but showed an overall increase. The 1960s accounts for the least, while the 2010s accounts for the most.\n",
    "\n",
    "**The revenue of high revenue movie shows a strong positive correlation with budget and popularity, and a weak correlation with average voting.\n",
    "\n",
    "**The most popular genre of the movie changed over the year, although it shows the stability in some periods.\n",
    "Over the year, animation, fantasy, and adventure account for a large proportion of the most popular genre.\n",
    "\n",
    "**The limitation of this research is that there are so many data that have been cleaned in this report. \n",
    "These datas are seen as anomalies since they contains NaN, duplicates, or 0 in some or all columns. The amount of data changed from 10866 to 3854. The change is huge so that the results may not represent the population.\n",
    "\n",
    "## Submitting your Project \n",
    "\n",
    "> **Tip**: Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).\n",
    "\n",
    "> **Tip**: Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.\n",
    "\n",
    "> **Tip**: Once you've done this, you can submit your project by clicking on the \"Submit Project\" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Reference\n",
    "1.https://stackoverflow.com/questions/50731229/split-cell-into-multiple-rows-in-pandas-dataframe\n",
    "\n",
    "2.https://stackoverflow.com/questions/31361599/with-pandas-in-python-select-the-highest-value-row-for-each-group\n",
    "\n",
    "3.https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py\n",
    "\n",
    "4.https://github.com/yinghaoz1/tmdb-movie-dataset-analysis/blob/master/tmdb-movie-dataset-analysis\n",
    "\n",
    "5.https://www.kaggle.com/code/mohamedabohassan/investigate-a-dataset-tmdb-movie\n",
    "\n",
    "6.https://praxitelisk.github.io/DAND-P1-Investigate-a-Dataset/Investigate_a_Dataset.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "255"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from subprocess import call\n",
    "call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
