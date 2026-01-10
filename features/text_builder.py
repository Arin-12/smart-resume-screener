def build_resume_text(df):
    df["Experience_Years_str"] = df["Experience_Years"].astype(str)

    df["resume_text"] = (
        df["Skills"] + " " +
        df["Current_Job_Title"] + " " +
        df["Previous_Job_Titles"] + " " +
        df["Target_Job_Description"] + " " +
        df["Degrees"] + " " +
        df["Field_of_Study"] + " " +
        df["Experience_Years_str"] + " years experience"
    )
    return df


def build_job_text(df):
    df["YearsOfExperience_str"] = df["YearsOfExperience"].astype(str)

    df["job_text"] = (
        df["Skills"] + " " +
        df["Title"] + " " +
        df["Responsibilities"] + " " +
        df["Keywords"] + " " +
        df["YearsOfExperience_str"] + " years experience"
    )
    return df
