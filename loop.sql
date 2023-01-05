DO $$
	DECLARE
		TestTeam_name team.team_name%TYPE;
		
	BEGIN
		TestTeam_name := 'TestName_';
		FOR counter IN 1..5
			LOOP
				INSERT INTO team (team_id, team_name)
            		VALUES (counter + 7, TestTeam_name || counter);
        	END LOOP;
 END;
 $$