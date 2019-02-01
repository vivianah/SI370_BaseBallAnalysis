# generate the 4 diagnostic plots given a series
def fourPlot( series ):
    sns.set(font_scale=1)
    fig, axs = plt.subplots(2,2)
    plt.tight_layout(pad=0.4, w_pad=4, h_pad=2.0)

    # Histogram
    sns.distplot(series, ax=axs[0,0])
    
    # Lag plot
    lag = series.copy()
    lag = np.array(lag[:-1])
    current = series[1:]
    ax = sns.regplot(current,lag,fit_reg=False, ax=axs[0,1])
    ax.set_ylabel("y_i-1")
    ax.set_xlabel("y_i")
    
    # QQ plot
    qntls, xr = stats.probplot(series, fit=False)
    sns.regplot(xr,qntls, ax=axs[1,0],ci=0)
    
    # Run sequence
    ax = sns.regplot(np.arange(len(series)),series, ax=axs[1,1],ci=0)
    ax.set_ylabel("val")
    ax.set_xlabel("i")
    sns.set(font_scale=1.5)
    
    