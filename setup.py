import cx_Freeze
executables = [cx_Freeze.Executable("Mastermind.py")]
cx_Freeze.setup(
    name="Mastermind",
    options={"build_exe": {"packages": ["pygame"]}},
    description="Mastermind interactive game",
    executables=executables
)
