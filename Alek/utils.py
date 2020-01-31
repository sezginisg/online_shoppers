def encoder_func(data):
    ohe = OneHotEncoder()
    encoded_vars = ohe.fit_transform(data).toarray()
    ohe_df = pd.DataFrame(encoded_vars, columns=ohe.get_feature_names(data.columns))
    print(f' The shape of the dataframe is: {ohe_df.shape}.')
