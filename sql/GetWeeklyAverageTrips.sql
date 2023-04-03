/****** Object:  StoredProcedure [dbo].[GetWeeklyAverageTrips]    Script Date: 01/04/2023 06:00:40 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[GetWeeklyAverageTrips]
    @startDate DATETIME2,
    @endDate DATETIME2
AS
BEGIN
	WITH avg_trips_cte AS (
		SELECT region, COUNT(*) as trips, DATEADD(wk, DATEDIFF(wk, 0, datetime), 0) as datetime
		    FROM trips
		    GROUP BY region, DATEADD(wk, DATEDIFF(wk, 0, datetime), 0)
			)

	SELECT region, DATEPART(wk, datetime) as week_number, AVG(trips) as avg_trips
	FROM avg_trips_cte
	WHERE datetime >= @startDate AND datetime < @endDate
	GROUP BY region, DATEPART(wk, datetime)

END
GO


