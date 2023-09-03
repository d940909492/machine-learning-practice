using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.AI;
using UnityEngine.AI;

public class nav_test : MonoBehaviour
{
    [SerializeField] private Transform movingTarget;

    private NavMeshAgent navmeshagent;
    private void Awake()
    {
        navmeshagent = GetComponent<NavMeshAgent>();
    }

    // Update is called once per frame
    void Update()
    {
        navmeshagent.destination = movingTarget.position;
    }
}
