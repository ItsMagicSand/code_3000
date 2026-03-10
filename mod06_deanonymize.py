import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    identifiers = ['age', 'zip3', 'gender']
    combined = pd.merge(anon_df, aux_df, col = identifiers, type = 'inner')
    res = combined[['anon_id', 'name']].copy()
    return res

def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    raise NotImplementedError
