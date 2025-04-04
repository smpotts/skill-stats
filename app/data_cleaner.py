import json
import logging

logging.basicConfig(level=logging.INFO)

class DataCleaner:
    # pass the file paths in as arguments or store them in a config
    def __init__(self, proficiency_path, skills_path, data_path):
        self.proficiency_path = proficiency_path
        self.skills_path = skills_path
        self.data_path = data_path

        # initialize the cleaned data to blank
        self.clean_proficiency = []
        self.clean_skills = []
        self.clean_data = []
    
    def _read_source_file(self, filename):
        try:
            with open(filename, 'r') as file:
                raw_data = json.load(file)
                return raw_data
        except Exception as e:
            logging.error(f"Exception reading {filename}: {e}.") 


    def _validate_keys(self, record, expected_keys):
        # check if the keys in the json record matches the expected keys
        return set(record.keys()) == expected_keys


    def consume_raw_data_file(self):
        raw_data = self._read_source_file(self.data_path)
        # handle the case where the file read is successful, but the file itself is empty
        # the file might contain an empty list, null, or some malformed data
        if not raw_data:
            return

        records = raw_data.get('scores', [])
        for record in records:   
            if self._validate_keys(record, record.keys()):
                skill = record.get("skill")
                score = record.get("score")

                # making sure the values match the type we expect
                if isinstance(skill, str) and len(skill) == 1 and isinstance(score, int):
                    self.clean_data.append(record)
        
        logging.info(f"Cleaned {len(self.clean_data)} records from {self.data_path}.")


    def consume_raw_proficiency_file(self):
        raw_profs = self._read_source_file(self.proficiency_path)
        if not raw_profs:
            return

        self.clean_proficiency = [
            record for record in raw_profs.get("proficiency", [])
            if record is not None and isinstance(record, int)
        ]

        logging.info(f"Cleaned {len(self.clean_proficiency)} records from {self.proficiency_path}.")


    def consume_raw_skills_file(self):
        raw_skills = self._read_source_file(self.skills_path)
        if not raw_skills:
            return

        self.clean_skills = [
            record for record in raw_skills.get("skills", [])
            if self._validate_keys(record, record.keys())
            if isinstance(record["skill"], str) and len(record["skill"]) == 1 
        ]

        logging.info(f"Cleaned {len(self.clean_skills)} records from {self.skills_path}.")


    def process(self):
        logging.info("Starting data processing...")
        self.consume_raw_data_file()
        self.consume_raw_skills_file()
        self.consume_raw_proficiency_file()
        logging.info("Data processing complete!")
