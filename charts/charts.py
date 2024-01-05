from matplotlib import pyplot as plt
import streamlit as st


def plot_value_counts(df, column):
    value_counts = df[column].value_counts()
    fig, ax = plt.subplots(figsize=(8, 6))  # Set the size of the plot
    bars = value_counts.plot(kind='bar', ax=ax)
    ax.set_title(f'Count of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Count')

    # Add text annotations to each bar
    for i, val in enumerate(value_counts):
        plt.text(i, val + 1, str(val), ha='center', va='bottom')

    st.pyplot(fig)


def plot_value_counts_within_interval(df, column, interval):
    filtered_data = df[(df[column] >= interval[0]) & (df[column] <= interval[1])]
    if column == 'salaire':
        return filtered_data[column].describe()
    value_counts = filtered_data[column].value_counts()

    fig, ax = plt.subplots(figsize=(10, 8))
    value_counts.plot(kind='bar', ax=ax)
    ax.set_title(f'Count of {column} within Interval {interval}')
    ax.set_xlabel(column)
    ax.set_ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    for i, val in enumerate(value_counts):
        plt.text(i, val + 1, str(val), ha='center', va='bottom')

    st.pyplot(fig)

    return filtered_data[column].describe()
