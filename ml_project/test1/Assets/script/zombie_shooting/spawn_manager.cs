using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class spawn_manager : MonoBehaviour
{
    public GameObject objectToSpawn;
    public int maxSpawnNumber = 5;
    public float spawnTime = 2f;
    public Vector3 spawnAreaSize = new Vector3(25f, 1.5f, 25f);
    public ml_test mltest;

    private int currentSpawnCount = 0;

    private void Start()
    {
        InvokeRepeating("SpawnObject", 0f, spawnTime);
        mltest.addEnemy();
    }

    private void SpawnObject()
    {
        if (currentSpawnCount >= maxSpawnNumber)
        {
            CancelInvoke("SpawnObject");
            return;
        }

        Vector3 randomSpawnPosition = new Vector3(
            Random.Range(-spawnAreaSize.x / 2f, spawnAreaSize.x / 2f),
            transform.position.y,
            Random.Range(-spawnAreaSize.z / 2f, spawnAreaSize.z / 2f)
        );

        GameObject spawnedObject = Instantiate(objectToSpawn, transform.position + randomSpawnPosition, Quaternion.identity);
        mltest.enemies.Add(spawnedObject.transform);

        currentSpawnCount++;
    }

    public void resetNumber()
    {
        currentSpawnCount = 0;
    }
}
