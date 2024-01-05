def filtredf(df, specealite, sexe, niveau, dispo, cheuveuxcolor):
    filtered = df.copy()  # Make a copy of the original DataFrame

    # Filter by 'specialite' if 'specialite' is selected
    if specealite:
        filtered = filtered[filtered['specialite'].isin(specealite)]

    # Filter by 'sexe' if 'sexe' is selected
    if sexe:
        filtered = filtered[filtered['sexe'].isin(sexe)]

    # Filter by 'diplome' if 'diplome' is selected
    if niveau:
        filtered = filtered[filtered['diplome'].isin(niveau)]

    # Filter by 'dispo' if 'dispo' is selected
    if dispo:
        filtered = filtered[filtered['dispo'].isin(dispo)]

    # Filter by 'cheveux' if 'cheveux' is selected
    if cheuveuxcolor:
        filtered = filtered[filtered['cheveux'].isin(cheuveuxcolor)]

        # Calculate value counts for specified metrics


    return filtered