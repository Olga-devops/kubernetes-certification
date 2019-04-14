# Task one 

_Set configuration context:_$ kubectl config use-context k8s
A Pod is running on the cluster but it is not responding.
The desired behavior is to have Kubernetes restart the pod when an endpoint returns an HTTP 500 on the `/healthz` endpoint. The service, liveness-http, should never send traffic to the Pod while it is failing. Please complete the following:


* The application has an endpoint, `/started`, that will indicate if it can accept traffic by returning an HTTP 200. If the endpoint returns an HTTP 500, the application has not yet finished initialization
* The application has another endpoint `/healthz` that will indicate if the application is still working as expected by returning an HTTP 200. If the endpoint returns an HTTP 500 the application is no longer responsive
* Configure the liveness-http Pod provided to use these endpoints
* The probes should use port 8080
*  image: fsadykov/kubernetes-certification:taskone.latest

