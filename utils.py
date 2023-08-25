import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def count_stat(vector):
    # We get '0' and '1' so run the frequency for each vector
    unique, counts = np.unique(vector, return_counts=True)
    return dict(zip(unique, counts))


def descriptive_stat_threshold(df,
                                pred_score,
                                threshold):
    # Find out how many 0 and 1

    
    # Now let's show the summary statistics:
    df = pd.DataFrame(df)
    
    df['Anomaly_Score'] = pred_score
    df['Group'] = np.where(df['Anomaly_Score'] < threshold, 'Normal', 'Outlier')

    # Summary Statistics

    l = [col for col in df.columns if str(col).isdigit()]


    agg_dict = {}
    for col in l:
             agg_dict[str(col)] = (col, "mean")


    agg_dict['count'] = ("Anomaly_Score", "count")
    agg_dict['Anomaly_Score'] = ("Anomaly_Score", "mean")

    stat = df.groupby('Group', as_index=False).agg(**agg_dict).assign(count_perc=lambda x: (x['count'] / x['count'].sum()) * 100).round({'mean': 2})

    return stat


def confusion_matrix(actual, score, threshold):
    actual_pred = pd.DataFrame({'actual': actual, 'pred': score})

    actual_pred['pred'] = np.where(actual_pred['pred'] <= threshold, 0, 1)

    cm = pd.crosstab(actual_pred['actual'], actual_pred['pred'])
    
    return cm

def plot_data(X_train_pd, y_train):
    plt.scatter(X_train_pd[0], X_train_pd[1],c=y_train, alpha=0.8)
    plt.title('Scatter plot')
    plt.xlabel('x0')
    plt.ylabel('x1')
    plt.show()