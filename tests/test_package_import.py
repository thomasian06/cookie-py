"""Test importing `{{ cookiecutter.package_name }}`."""

def test_import_{{ cookiecutter.package_name }}() -> None:
    """
    Test importing `{{ cookiecutter.package_name }}`.

    GIVEN: A valid import of {{ cookiecutter.package_name }}
    WHEN: {{ cookiecutter.package_name }} is imported
    THEN: {{ cookiecutter.package_name }} has the correct name
    """
    import {{ cookiecutter.package_name }}
    assert {{ cookiecutter.package_name }}.__name__ == "{{ cookiecutter.package_name }}"
