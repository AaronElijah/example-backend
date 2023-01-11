from subprocess import check_call


def delete_origin_feature_tags() -> None:
    # check_call(["git", "push", "-d", "origin", "$(", "git", "tag", "-l", "'*-a.*'", ")"])
    check_call(["git", "tag", '-d', '$(git tag -l "*-a.*")'])
