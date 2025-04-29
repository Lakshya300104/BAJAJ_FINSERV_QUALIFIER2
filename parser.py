import re

def is_numeric_line(line):
    return bool(re.fullmatch(r"[-+]?[\d\s\[\]./%uLmgdfl]+", line.strip(), re.IGNORECASE))

def parse_lab_results(lines):
    parsed_data = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        value_unit_match = re.search(r"([-+]?\d*\.?\d+)\s*([a-zA-Z/%μu]+)", line)

        if value_unit_match:
            test_value = value_unit_match.group(1)
            test_unit = value_unit_match.group(2)
            test_name = "Unknown"
            for j in range(i - 1, max(i - 4, -1), -1):  # Look back up to 3 lines
                candidate = lines[j].strip()
                if not is_numeric_line(candidate) and len(candidate.split()) <= 8:
                    test_name = candidate
                    break

            ref_low, ref_high = None, None
            if i + 1 < len(lines):
                ref_line = lines[i + 1].strip()
                ref_match = re.search(r"(\d*\.?\d+)[-–—](\d*\.?\d+)", ref_line)
                if ref_match:
                    ref_low = float(ref_match.group(1))
                    ref_high = float(ref_match.group(2))

            if ref_low is not None and ref_high is not None:
                value = float(test_value)
                lab_test_out_of_range = value < ref_low or value > ref_high

                parsed_data.append({
                    "test_name": test_name,
                    "test_value": test_value,
                    "bio_reference_range": f"{ref_low}-{ref_high}",
                    "test_unit": test_unit,
                    "lab_test_out_of_range": lab_test_out_of_range
                })

                i += 2
            else:
                i += 1
        else:
            i += 1

    return parsed_data
