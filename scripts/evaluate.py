#Author: Ioannis Anastopoulos
from sklearn.metrics import r2_score,confusion_matrix, accuracy_score,roc_curve,auc,precision_recall_fscore_support,f1_score
from scipy.stats import pearsonr
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def rmse(y_true, y_pred):
    return np.sqrt(np.mean(np.square(y_pred - y_true)))

def F_score(Y_true,predict_classes ,classes=None, plot=False,average=None):
    if classes is None:
        classes=range(len(set(Y_true)))
    eval_metrics_matrix=precision_recall_fscore_support(Y_true,predict_classes,labels=classes,average=average)
    f_score_df=pd.DataFrame(eval_metrics_matrix[2], columns=['F_score'],index=classes)
    f_score_df=f_score_df.drop_duplicates()

    if plot:
        plt.figure(figsize=(10,10))
        ax=f_score_df.plot(kind='bar', figsize=(7,10))
        for p in ax.patches:
            ax.annotate(str(round(p.get_height(),2)), (p.get_x() * 1.005, p.get_height() * 1.005))
        plt.title('F1_score')
        plt.show()
        plt.close()
    return f_score_df

def confusion(Y_true,predict_classes,classes=None,plot=False, title='Confusion Matrix',fontsize=16,cmap='tab20',normalize=False):

    if classes is None:
        classes=range(len(set(predict_classes)))

    conf_matrix=confusion_matrix(Y_true, predict_classes, labels=classes)

    if normalize:
        total=conf_matrix.sum(axis=0) #summing actual predictions
        conf_matrix= conf_matrix/total

    df_cm = pd.DataFrame(conf_matrix, index=classes,
                  columns=classes)
    #sns.set(font_scale=5)#for label size
    if plot:
        plt.figure(figsize=(10,10))
        sns.heatmap(df_cm, annot=True,annot_kws={"size":fontsize*(1/2) },cmap=cmap)# font size
        #fig=conf_hm.get_figure()
        plt.yticks(fontsize=fontsize+4)
        plt.xticks(fontsize=fontsize+4)
        plt.title(title, fontsize=fontsize+10)
        #fig.savefig(out,dpi=300)
        plt.show()
        plt.close()

    return conf_matrix

def to_categorical(y, num_classes):
    """ 1-hot encodes a tensor """
    return np.eye(num_classes, dtype='uint8')[y]

def ROC(y_true, y_pred,classes=None,title=None,plot=False):

    plt.figure(figsize=(10,10))
    lw=4

    if isinstance(y_true, pd.DataFrame):
        y_true=y_true.values
    if isinstance(y_pred, pd.DataFrame):
        y_pred=y_pred.values


    if classes is None:
        classes=set(y_true) #removing dups

    if len(classes)>2:
        y_true = to_categorical(y_true, len(classes))
        y_pred = to_categorical(y_pred, len(classes))
        fpr = dict()
        tpr = dict()
        roc_auc = dict()

        for i,cl in enumerate(classes):
            fpr[cl], tpr[cl], _ = roc_curve(y_true[:,i], y_pred[:, i])
            roc_auc[cl] = auc(fpr[cl], tpr[cl])
        
        if plot: 
            colors = plt.cm.get_cmap('tab20',len(classes)) #best line of code IN THE UNIVERSE

            for i, color in zip(range(len(classes)), colors.colors):
                cl = classes[i]
                plt.plot(fpr[cl], tpr[cl], color=colors.colors[i], lw=lw,
                     label='ROC curve of class {0} (area = {1:0.2f})'
                     ''.format(cl, roc_auc[cl]))
            plt.plot([0, 1], [0, 1], 'k--', lw=lw)
            plt.xlim([-0.03, 1.05])
            plt.ylim([-0.03, 1.05])
            plt.xlabel('False Positive Rate', fontsize=10)
            plt.ylabel('True Positive Rate',fontsize=10)
            plt.title(title, fontsize=12)
            plt.xticks(fontsize=10)
            plt.yticks(fontsize=10)
            plt.legend(loc="lower right",prop={'size': 15})
            #plt.savefig('/projects/sysbio/users/ianastop/cm_region_results/plots/%s_ROC.png'%self.out,dpi=300)
            plt.show()
            plt.close()

        return (fpr, tpr, roc_auc)

    else:
        fpr, tpr, _ = roc_curve(y_true, y_pred)
        roc_auc = auc(fpr, tpr)
        if plot:
            plt.plot(fpr, tpr, color='darkorange', lw=4, label='ROC curve (area = %0.2f)' % roc_auc)

            plt.plot([0, 1], [0, 1], 'k--', lw=lw)
            plt.xlim([-0.03, 1.05])
            plt.ylim([-0.03, 1.05])
            plt.xlabel('False Positive Rate', fontsize=10)
            plt.ylabel('True Positive Rate',fontsize=10)
            plt.title(title, fontsize=12)
            plt.xticks(fontsize=10)
            plt.yticks(fontsize=10)
            plt.legend(loc="lower right",prop={'size': 10})
            #plt.savefig('/projects/sysbio/users/ianastop/cm_region_results/plots/%s_ROC.png'%self.out,dpi=300)
            return( fpr, tpr, roc_auc)
            plt.show()
            plt.close()
            
        return fpr,tpr,roc_auc


def regression_eval(y_true,y_pred, axis=None):
    '''
    Function computes pearson, r2 and rmse row wise or column wise
    Returns a list for each metric for each row or column

    axis =0/1 if the vector predicted has multiple rows and columns: for expression matrices
    if the vectors has multiple samples predicted for 1 variable : for drug response vector of each drug individually
    '''
    #calculating metrics on a per sample basis
    if axis ==0:
        r_list = []
        r2_list = []
        rmse_list = []
        for i, vec in enumerate(y_true):
            r_list +=[pearsonr(vec, y_pred[i])[0]]
            r2_list += [r2_score(vec, y_pred[i])]
            rmse_list += [rmse(vec,y_pred[i])]
        r = np.mean(r_list)
        r2 = np.mean(r2_list)
        rmse_score = np.mean(rmse_list)
    elif axis == 1:
        r_list = []
        r2_list = []
        rmse_list = []
        for i, vec in enumerate(y_true.T):
            r_list +=[pearsonr(vec, y_pred.T[i])[0]]
            r2_list += [r2_score(vec, y_pred.T[i])]
            rmse_list += [rmse(vec,y_pred.T[i])]
        r = np.mean(r_list)
        r2 = np.mean(r2_list)
        rmse_score = np.mean(rmse_list)
    elif axis is None:
        r, _ = pearsonr(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        rmse_score = rmse(y_true, y_pred)
    return r,r2,rmse_score

def classification_eval(y_true, y_pred,classes=None):
    acc = accuracy_score(y_true,y_pred)
    f1 = f1_score(y_true, y_pred, average='weighted')
    roc_auc = ROC(y_true, y_pred,classes=classes)[-1]
    
    return acc, f1, roc_auc
        
def node_classification_eval():
    pass 
