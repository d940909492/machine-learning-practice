using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.AI;
using UnityEngine.AI;

public class zombie_ai: MonoBehaviour
{
    [SerializeField] private Transform Target;

    private NavMeshAgent navmeshagent;
    private void Awake()
    {
        navmeshagent = GetComponent<NavMeshAgent>();
    }

    private void Start()
    {
        GameObject agentMain = GameObject.Find("agent_main");

        if (agentMain != null)
        {
            Target = agentMain.transform;
        }
        else
        {
            Debug.LogError("GameObject with the name 'agent_main' not found.");
        }
    }

    // Update is called once per frame
    void Update()
    {
        navmeshagent.destination = Target.position;
    }
}
