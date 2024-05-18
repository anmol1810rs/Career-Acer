**Kubernetes Interview Preparation MCQs**

**Easy Level**

Q1. What is Kubernetes?
A) A video streaming platform
B) A container orchestration tool
C) A type of hardware
D) A programming language  
**Answer: B) A container orchestration tool**

Q2. Which of the following can Kubernetes manage?
A) Only Docker containers
B) Any type of containers
C) Only virtual machines
D) Only physical servers  
**Answer: B) Any type of containers**

Q3. What does the term 'Pod' in Kubernetes refer to?
A) A collection of network policies
B) A single instance of a running process in Kubernetes
C) A group of one or more containers
D) A Kubernetes storage unit  
**Answer: C) A group of one or more containers**

Q4. Which command is used to get information about all the pods in Kubernetes?
A) kubectl get pods
B) kubectl see pods
C) kubectl collect pods
D) kubectl pods info  
**Answer: A) kubectl get pods**

Q5. What does K8s stand for?
A) 8 key components of Kubernetes
B) Kubernetes in 8 steps
C) Kubernetes, where '8' stands for the number of letters between K and s
D) A new version of Kubernetes  
**Answer: C) Kubernetes, where '8' stands for the number of letters between K and s**

**Medium Level**

Q6. Which of the following is a primary component of Kubernetes architecture?
A) Node
B) Pod
C) ReplicaSet
D) All of the above  
**Answer: D) All of the above**

Q7. What is the role of 'etcd' in Kubernetes?
A) Data visualization
B) Load balancing
C) Backup service
D) Key-value store for cluster data  
**Answer: D) Key-value store for cluster data**

Q8. How does Kubernetes handle service discovery?
A) Using environment variables
B) Using a proprietary service discovery protocol
C) Kubernetes cannot discover services
D) Both A and DNS-based methods  
**Answer: D) Both A and DNS-based methods**

Q9. What is a 'Namespace' in Kubernetes?
A) A way to divide cluster resources between multiple users
B) A type of storage class
C) A networking policy
D) A method to load balance  
**Answer: A) A way to divide cluster resources between multiple users**

Q10. What is the purpose of a Kubernetes Deployment?
A) To provide a stable network for applications
B) To orchestrate the build process of images
C) To manage stateful applications
D) To manage the deployment and scaling of a set of Pods  
**Answer: D) To manage the deployment and scaling of a set of Pods**

**Hard Level**

Q11. What is Helm in Kubernetes?
A) A package manager for Kubernetes
B) A tool for automatic scaling
C) A security tool
D) A network configuration tool  
**Answer: A) A package manager for Kubernetes**

Q12. What does the term 'Ingress' refer to in Kubernetes?
A) Incoming network traffic rules
B) The process of removing a node
C) Internal pod scaling mechanism
D) Data encryption method  
**Answer: A) Incoming network traffic rules**

Q13. Which of the following statements is true about StatefulSets?
A) It is the same as a Deployment
B) It is used for stateless applications
C) It manages the deployment and scaling of a set of Pods, and provides guarantees about the ordering and uniqueness of these Pods
D) It does not support persistent storage  
**Answer: C) It manages the deployment and scaling of a set of Pods, and provides guarantees about the ordering and uniqueness of these Pods**

Q14. How does Kubernetes achieve auto-scaling?
A) Through manual intervention only
B) Using Horizontal Pod Autoscaler
C) By using StatefulSets
D) Kubernetes does not support auto-scaling  
**Answer: B) Using Horizontal Pod Autoscaler**

Q15. What is a 'Service' in Kubernetes?
A) A way to expose an application running on a set of Pods
B) A single configuration file
C) A batch job scheduler
D) A type of deployment strategy  
**Answer: A) A way to expose an application running on a set of Pods**

**Extreme Level**

Q16. How do you handle persistent storage in Kubernetes?
A) PersistentVolumes and PersistentVolumeClaims
B) Only with StatefulSets
C) Using Ingress controllers
D) With ConfigMaps only  
**Answer: A) PersistentVolumes and PersistentVolumeClaims**

Q17. What is the role of a 'Sidecar' container in a Pod?
A) To enhance or extend the main container's functionalities
B) To replace a failing container
C) To manage storage
D) To perform health checks on the main container  
**Answer: A) To enhance or extend the main container's functionalities**

Q18. Describe the term 'DaemonSet' in Kubernetes.
A) Ensures only one pod runs across the cluster
B) Ensures that some or all nodes run a copy of a Pod
C) Manages stateful applications
D) Is used for batch jobs only  
**Answer: B) Ensures that some or all nodes run a copy of a Pod**

Q19. What is the significance of 'kubectl drain' command?
A) To remove all pods from a node
B) To add pods to a node
C) To check the status of a node
D) To update the Kubernetes version on a node  
**Answer: A) To remove all pods from a node**

Q20. What is the primary benefit of using 'Custom Resource Definitions' (CRDs) in Kubernetes?
A) To modify existing resource types
B) To create new, custom resources that extend the Kubernetes API
C) To delete default resource types
D) To merge multiple resources into a single one  
**Answer: B) To create new, custom resources that extend the Kubernetes API**