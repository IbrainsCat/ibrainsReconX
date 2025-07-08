def verify_license(input_key):
    valid_keys = [
        "IBRAINS-ALPHA-001",
        "IBRAINS-BETA-002",
        "IBRAINS-ELITE-003"
    ]
    return input_key in valid_keys
