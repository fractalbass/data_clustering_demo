import pandas as pd
import numpy as np
from Utilities import Utilities
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pylab import *
import matplotlib.cm as cm


class DataClusterDemo:

    def run(self):
        #  Create a CSV file that we can read into a dataframe.
        util = Utilities()
        util.convert_json_file("kc_aggravated_assault_2017.json", "kcav.csv")
        kc_data = pd.read_csv("kcav.csv")

        #  Split the dataframe in lat and long series.
        f1 = kc_data['lat'].values
        f2 = kc_data['lon'].values

        #  Define the number of clusters we want
        cluster_num = 8

        #  Discover the clusters
        kmeans = KMeans(n_clusters=cluster_num).fit(kc_data)
        cluster_labels = kmeans.fit_predict(kc_data)
        centroids = kmeans.cluster_centers_
        colors = 0.5 + (0.5*(cm.spectral(cluster_labels.astype(float) / cluster_num)))

        # "Underlay the map below the points.
        img = plt.imread("KC_Map.png")
        fig, ax = plt.subplots()
        ax.imshow(img, extent=[-94.9013, -94.2054, 38.9214, 39.2158, ])

        # Display the actual data points on the map.  Note that our data is in the format of latitude, longitude.
        # We need to plot these in reverse order to translate them to the X and Y axis.
        plt.scatter(f2,f1, c=colors)

        #Put a black circle in the middle of each cluster (a.k.a. centroid)
        for c in centroids:
            c = plt.Circle((c[1],c[0]),0.01, color='black')
            ax.add_artist(c)

        # Display everything.  Because we are running this in pycharm, we set block to TRUE.  This
        # prevents the map window from closing right away.
        plt.show(block=True)

dcd = DataClusterDemo()
dcd.run()