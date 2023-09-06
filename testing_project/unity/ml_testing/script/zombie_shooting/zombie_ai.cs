using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class zombie_ai : MonoBehaviour
{
    private Transform Target;
    private NavMeshAgent navmeshagent;

    private void Awake()
    {
        navmeshagent = GetComponent<NavMeshAgent>();
    }

    private void Start()
    {
        FindClosestTarget();
    }

    void FindClosestTarget()
    {
        GameObject[] agentMainObjects = GameObject.FindGameObjectsWithTag("agent_main");

        if (agentMainObjects.Length > 0)
        {
            Transform closestTarget = null;
            float closestDistance = Mathf.Infinity;

            foreach (GameObject agentMainObject in agentMainObjects)
            {
                float distance = Vector3.Distance(transform.position, agentMainObject.transform.position);
                if (distance < closestDistance)
                {
                    closestDistance = distance;
                    closestTarget = agentMainObject.transform;
                }
            }

            Target = closestTarget;
        }
        else
        {
            Debug.LogError("No GameObjects with the tag 'agent_main' found.");
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (Target != null)
        {
            navmeshagent.destination = Target.position;
        }
    }
}
