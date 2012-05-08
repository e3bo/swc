SELECT Project.ProjectName,COUNT(DISTINCT Involved.Login) from Project join Involved where (Project.ProjectId = Involved.ProjectId) group by Project.ProjectId;
