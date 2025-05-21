
# sp["adj_close_normalized"] = (sp["adj_close"] - sp["adj_close"].min()) / (
#     sp["adj_close"].max() - sp["adj_close"].min()
# )
# df["adj_close_normalized"] = (df["adj_close"] - df["adj_close"].min()) / (
#     df["adj_close"].max() - df["adj_close"].min()
# )

# ## Filter the dataframes to only include the dates that are present in both
# shared_indices = df.index.intersection(sp.index)
# df_filtered = df.loc[shared_indices]
# sp_filtered = sp.loc[shared_indices]

# ## Calculate the first and second derivatives for both dataframes
# df_filtered["first_derivative"] = df_filtered["adj_close_normalized"].diff()
# df_filtered["second_derivative"] = df_filtered["first_derivative"].diff()

# sp_filtered["first_derivative"] = sp_filtered["adj_close_normalized"].diff()
# sp_filtered["second_derivative"] = sp_filtered["first_derivative"].diff()


# ## Merge the dataframes on the shared indices
# merged_second_derivatives = pd.concat(
#     [
#         df_filtered["second_derivative"].rename("AMZN_second_derivative"),
#         sp_filtered["second_derivative"].rename("SPX_second_derivative"),
#         df_filtered["adj_close"].rename("AMZN_adj_close"),
#         sp_filtered["adj_close"].rename("SPX_adj_close"),
#     ],
#     axis=1,
# )

# ## Drop rows with NaN values
# merged_second_derivatives.dropna(inplace=True)

# ## Calculate the Mean Squared Error (MSE)
# MSE = np.square(
#     np.subtract(
#         merged_second_derivatives["AMZN_second_derivative"],
#         merged_second_derivatives["SPX_second_derivative"],
#     )
# ).mean()