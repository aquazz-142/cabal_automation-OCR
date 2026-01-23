# Arrival skill stats and data
# Migrated from arrival_skill_ocr/stats_data.py

# Known skill options
KNOWN_SKILLS = [
    # Offensive stats
    "All Skill Amp. UP",
    "Ignore Resist Skill Amp.",
    "All Attack Up.",
    "Add. Damage",
    "Critical DMG.",
    "Ignore Resist Crit. DMG",
    "Arrival Skill Cool Time decreased.",
    "Ignore Resist Critical Rate",
    "Ignore Evasion",
    "Attack Rate",
    "Resist Skill Amp",
    "Arrival Skill Buff Time UP",
    "Max Critical Rate",
    "Accuracy",
    "Cancel Ignore Penetration",
    "Normal DMG Up",
    "Ignore Penetration",
    "Penetration",

    # Defensive stats
    "HP Auto Heal",
    "Absorb Damage",
    "HP Absorb Up",
    "Max HP Steal per Hit",
    "Defense",
    "DMG Reduction",
    "Heal",
    "Ignore Accuracy",
    "Defense Rate",
    "Resist Crit. DMG",
    "Evasion",
    "PvE Resist Skill Amp.",
    "PvE Resist Crit. DMG",
    "Damage Absorb"
]

# Categorize skills
OFFENSIVE_SKILLS = [
    "All Skill Amp. UP",
    "Ignore Resist Skill Amp.",
    "All Attack Up. (1)",
    "All Attack Up. (2)",
    "All Attack Up. (3)",
    "Add. Damage (1)",
    "Add. Damage (2)",
    "Critical DMG.",
    "Ignore Resist Crit. DMG",
    "Arrival Skill Cool Time decreased.",
    "Ignore Resist Critical Rate",
    "Ignore Evasion",
    "Attack Rate (1)",
    "Attack Rate (2)",
    "Resist Skill Amp",
    "Arrival Skill Buff Time UP",
    "Max Critical Rate",
    "Accuracy",
    "Cancel Ignore Penetration",
    "Normal DMG Up",
    "Ignore Penetration",
    "Penetration"
]

DEFENSIVE_SKILLS = [
    "HP Auto Heal",
    "Absorb Damage (1)",
    "Absorb Damage (2)",
    "Absorb Damage (3)",
    "HP Absorb Up",
    "Max HP Steal per Hit (1)",
    "Max HP Steal per Hit (2)",
    "Defense",
    "DMG Reduction",
    "Heal (1)",
    "Heal (2)",
    "Ignore Accuracy",
    "Defense Rate",
    "Resist Critical Damage",
    "Evasion",
    "PvE Resist Skill Amp.",
    "PvE Resist Crit. DMG",
    "Damage Absorb"
]

# Mapping for display names to base names for OCR detection
DISPLAY_TO_BASE = {
    "All Attack Up. (1)": "All Attack Up.",
    "All Attack Up. (2)": "All Attack Up.",
    "All Attack Up. (3)": "All Attack Up.",
    "Add. Damage (1)": "Add. Damage",
    "Add. Damage (2)": "Add. Damage",
    "Attack Rate (1)": "Attack Rate",
    "Attack Rate (2)": "Attack Rate",
    "Absorb Damage (1)": "Absorb Damage",
    "Absorb Damage (2)": "Absorb Damage",
    "Absorb Damage (3)": "Absorb Damage",
    "Max HP Steal per Hit (1)": "Max HP Steal per Hit",
    "Max HP Steal per Hit (2)": "Max HP Steal per Hit",
    "Heal (1)": "Heal",
    "Heal (2)": "Heal"
}

# Stat variations with their possible values
STAT_VARIATIONS = {
    # Offensive stats
    "All Skill Amp. UP": ["4%", "8%", "16%"],
    "Ignore Resist Skill Amp.": ["3%", "5%", "9%"],
    "All Attack Up. (1)": ["15", "30", "45", "60", "75"],
    "All Attack Up. (2)": ["18", "36", "54", "72", "90"],
    "All Attack Up. (3)": ["25", "50", "75", "90", "125"],
    "Add. Damage (1)": ["15", "30", "45", "60", "75"],
    "Add. Damage (2)": ["18", "36", "54", "72", "90"],
    "Critical DMG.": ["9%", "18%", "36%"],
    "Ignore Resist Crit. DMG": ["6%", "11%", "20%"],
    "Arrival Skill Cool Time decreased.": ["15s", "30s", "60s", "120s"],
    "Ignore Resist Critical Rate": ["1%", "2%"],
    "Ignore Evasion": ["100", "200", "300", "400", "500"],
    "Attack Rate (1)": ["100", "200", "300", "400", "500"],
    "Attack Rate (2)": ["120", "240", "300", "360", "480", "600"],
    "Resist Skill Amp": ["8%", "15%", "30%"],
    "Arrival Skill Buff Time UP": ["4s", "8s", "16s", "30s"],
    "Max Critical Rate": ["1%", "2%"],
    "Accuracy": ["120", "240", "300", "360", "480", "600"],
    "Cancel Ignore Penetration": ["18", "35", "75"],
    "Normal DMG Up": ["8%", "16%", "24%", "32%", "40%"],
    "Ignore Penetration": ["50", "100", "200"],
    "Penetration": ["30", "65", "130"],

    # Defensive stats
    "HP Auto Heal": ["120", "240", "500"],
    "Absorb Damage (1)": ["600", "1,200", "2,400"],
    "Absorb Damage (2)": ["800", "1,600", "3,200"],
    "Absorb Damage (3)": ["900", "1800", "4500"],
    "HP Absorb Up": ["1%", "2%", "3%", "4%", "5%"],
    "Max HP Steal per Hit (1)": ["6", "12", "18", "24", "30"],
    "Max HP Steal per Hit (2)": ["7", "14", "21", "28", "35"],
    "Defense": ["100", "200", "400"],
    "DMG Reduction": ["15", "30", "45", "60", "75"],
    "Heal (1)": ["200", "400", "600"],
    "Heal (2)": ["300", "600", "900"],
    "Ignore Accuracy": ["80", "160", "240", "320", "400"],
    "Defense Rate": ["80", "160", "240", "320", "400"],
    "Resist Critical Damage": ["18%", "35%", "70%"],
    "Evasion": ["90", "180", "270", "360", "450"],
    "PvE Resist Skill Amp.": ["1%", "2%", "3%", "4%", "5%"],
    "PvE Resist Crit. DMG": ["2%", "4%", "6%", "8%", "10%"],
    "Damage Absorb": ["900", "1800", "4500"]
}

def get_all_skills():
    """Get all available skills"""
    return KNOWN_SKILLS

def get_offensive_skills():
    """Get all offensive skills"""
    return OFFENSIVE_SKILLS

def get_defensive_skills():
    """Get all defensive skills"""
    return DEFENSIVE_SKILLS

def get_stat_variations(stat_name):
    """Get possible variations for a specific stat"""
    return STAT_VARIATIONS.get(stat_name, [])

def get_all_stat_variations():
    """Get all stat variations dictionary"""
    return STAT_VARIATIONS

def get_base_stat_name(display_name):
    """
    Get the base stat name for OCR detection from a display name.
    For duplicate stats, this returns the common base name used for detection.
    """
    return DISPLAY_TO_BASE.get(display_name, display_name)

def get_all_base_stat_names():
    """Get all unique base stat names for OCR detection"""
    return list(set(KNOWN_SKILLS + [DISPLAY_TO_BASE.get(stat, stat) for stat in OFFENSIVE_SKILLS + DEFENSIVE_SKILLS]))
