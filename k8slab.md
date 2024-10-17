# **Workshop: Creating Kubernetes Deployment and Service Files**

## **Workshop Overview**
In this session Hummingbirds will learn how to translate a Docker Compose file into Kubernetes resources, specifically **Deployments** and **Services**, using `kubectl` commands. We will focus on two services from a provided Docker Compose file: `rest-proxy` and `frontend-fake-portal`. You will first create Kubernetes Deployments and Services using `kubectl` commands and then convert those resources into YAML files for future use.

The workshop will be split into the following sections:
1. Using `kubectl` to create Deployments and Services for `rest-proxy` and `frontend-fake-portal`
2. Converting your working Kubernetes resources into YAML files
3. Validating the Kubernetes resources using provided `redis` and `report-service` Kubernetes files

## **GOAL OF TODAY**
In the following section you will find the steps that were made to create the `redis.yml` and the `reporting-service.yaml`, your goal is to generate the YAML files for the rest-proxy and the frontend-fake-portal. Please divide in two teams and try to do something similar for one of the services. 10 minutes before ending the session push your changes and lets try to deploy all the services together.

### **Create Deployment and Service for `redis`**

1. **Deploy the `redis` Service**:
   - Use `kubectl` to create the deployment with the following command:
     ```bash
     kubectl create deployment redis --image=redis:latest --port=6379
     ```

2. **Expose the Deployment**:
   - Create a Service to expose the `redis` service on port 6379:
     ```bash
     kubectl expose deployment redis --type=ClusterIP --port=6379
     ```

3. **Verify the Deployment and Service**:
   - Check the deployment and service status:
     ```bash
     kubectl get deployments,services
     ```

### **Create Deployment and Service for `reporting-service`**

1. **Deploy the `reporting-service` Service**:
   - Use `kubectl` to create the deployment with the following command:
     ```bash
     kubectl create deployment report-service --image=report-service:production
     ```
2. To match the environment variables and ports from the Docker Compose file:

   ```bash

   kubectl set env deployment/report-service REDIS_HOST=redis REDIS_PORT=6379 NAME=report_service
   kubectl expose deployment report-service --port=50051
   ```

3. **Expose the Deployment**:
   - Create a Service to expose the `reporting-service` service on port 50051:
     ```bash
     kubectl expose deployment report-service --type=ClusterIP --port=50051
     ```

3. **Verify the Deployment and Service**:
   - Check the deployment status:
     ```bash
     kubectl get deployments
     ```
   - Verify the service is exposed:
     ```bash
     kubectl get services
     ```

## **Generating YAML Files for Redis and Report Service**

Now that the Kubernetes resources are running, we can generate the YAML configurations from the existing resources.

### **1. Exporting Redis Deployment YAML**
To generate the YAML for the Redis deployment:

```bash
kubectl get deployment redis -o yaml > redis-deployment.yaml
```

### **2. Exporting Redis Service YAML**
To generate the YAML for the Redis service, lets append it by the end of the redis-deployment.yaml:

```bash
kubectl get service redis -o yaml >> redis-deployment.yaml
```

### **3. Exporting Report Service Deployment YAML**
To generate the YAML for the Report Service deployment:

```bash
kubectl get deployment report-service -o yaml > report-service-deployment.yaml
```

### **4. Exporting Report Service YAML**
To generate the YAML for the Report Service service:

```bash
kubectl get service report-service -o yaml >> report-service-deployment.yaml
```

Now, you should have the following YAML files:
- `redis-deployment.yaml`
- `report-service-deployment.yaml`

## **Step 6: Reviewing and Refining the YAML Files**

Take a look at the generated YAML files. Here are some key sections to review:
1. **metadata**: Ensure that you remove the status sections, the resource ID and the UUID.


## **Apply YAML Files**

Once you’ve refined the YAML files, you can apply them to your Kubernetes cluster.

```bash
kubectl apply -f redis-deployment.yaml
kubectl apply -f report-service-deployment.yaml
```

## **Verify Your Deployments and Services**

After applying the YAML files, verify that everything is running smoothly.

```bash
kubectl get deployments
kubectl get services
```
