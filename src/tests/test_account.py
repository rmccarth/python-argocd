from python_argocd import Argo

def test_account_info():
    argo = Argo('https://20.72.171.128', 'admin', 'admin', verify=False)
    response = argo.account_info()
    assert isinstance(response, dict)

def test_can_i():
    # although the account is called 'admin' it actually can't do some things unless the configmap is altered. 
    argo = Argo('https://20.72.171.128', 'admin', 'admin', verify=False)
    response1 = argo.can_i("clusters", "get", None)
    response2 = argo.can_i("projects", "get", None)
    response3 = argo.can_i("applications", "get", None)
    response4 = argo.can_i("repositories", "get", None)
    response5 = argo.can_i("certificates", "get", None)
    response6 = argo.can_i("applications", "create", "*")

    assert response1['value'] == "yes"
    assert response2['value'] == "yes"
    assert response3['value'] == "no"
    assert response4['value'] == "yes"
    assert response5['value'] == "yes"
    assert response6['value'] == "no"



 
