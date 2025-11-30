from ln39 import M, utils


ln1 = [
    M("fileA", "~/39config/fileA"),
    M("dirA", "~/39config/dirA"),
    M("nofile", "~/39config/nofile"),
]

if utils.env_exists("LN1"):
    utils.ln(ln1)


# NOTE: ln 2
ln2 = [
    M("fileA", "~/39config/fileA"),
    M("nofile", "~/39config/nofile", enabled=False),
]

if utils.env_exists("LN2"):
    utils.ln(ln2)


# NOTE: fn
def before_ln(opts):
    print("opts.src:", opts.src)


def after_ln(opts):
    print("opts.dest:", opts.dest)


fn = [
    M("fileA", "~/39config/fn1", after_ln=after_ln),
    M("fileA", "~/39config/fn2", before_ln=before_ln),
]
if utils.env_exists("FUNC"):
    utils.ln(fn)


# NOTE: hang ln
hang = [
    M("fileA", "~/39config/ln.hang"),
]

if utils.env_exists("HANG"):
    utils.ln(hang)


# NOTE: backup file
bak = [
    M("fileA", "~/39config/fileA"),
    M("dirA", "~/39config/dirA"),
]
if utils.env_exists("BACKUP"):
    utils.ln(bak)


# NOTE: utils

if utils.env_exists("UTILS"):
    # env
    print(f"""get env: SHELL
{utils.get_env("SHELL")}
""")
    print(f"""env env_exists: SHELL
{utils.env_exists("SHELL")}
""")
    print(f"""env equal:  SHELL /bin/zsh
{utils.env_equals("SHELL", "/bin/zsh")}
""")
    # os
    print(f"""get os name:
{utils.get_os_name()}
""")
    print(f"""path for: 
{utils.path_for(linux="linux", macos="MacOS")}
""")

    res = utils.run(["ls", "-a"], cwd="~/Desktop/")
    print(f"""run: ls -a
          {res.stdout} """)
