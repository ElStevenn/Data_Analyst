import numpy as np
import matplotlib.pyplot as plt


class Elections_grafic_design:
    """
    Generate Scratter grpahic from independence parties
    """
    def __init__(self, pecentage_pro_independence, total_votes):
        # X = each town (auto_calculed)
        # Y = percentage_pro_indepen
        # Circle_size = total_votes

        self.X = np.arange(1, len(total_votes)+1)
        self.Y = np.array([a[0] for a in pecentage_pro_independence])
        self.Circle_size = total_votes

        self.total_votes = total_votes

        print(self.X)
        print(self.Y)
        print(self.Circle_size)


   
    def ord_data(self):
        print(self.Y)




    def build_scatter(self):
        plt.style.use('_mpl-gallery')

        sizes = self.total_votes  * 0.2 if len(self.total_votes) > 20000 elif :
            
        colors = np.random.uniform(15, 80, len(self.X))

        fix, ax = plt.subplots()

        ax.scatter(self.X, self.Y, s=sizes, c=colors, vmin=0)

        plt.show()


def testing():
    plt.style.use('_mpl-gallery')
    
    y = np.array([20,40,20,30,50])
    x = np.arange(1,len(y)+1)
    
    sizes = np.random.uniform(15, 80, len(x))
    colors = np.random.uniform(15, 80, len(x))
    # Plot
    fix, ax = plt.subplots()

    print(sizes)


    ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=10)

    plt.plot()
    
    plt.show()


if __name__ == '__main__':
    testing()

