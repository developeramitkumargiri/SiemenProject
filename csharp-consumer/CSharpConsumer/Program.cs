using System;
using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;
using System.Collections.Generic;

class Program
{
    static async Task Main()
    {
        using HttpClient client = new();

        bool isReady = false;
        while (!isReady)
        {
            try
            {
                var response = await client.GetAsync("http://fastapi-service:5000/data");

                if (response.IsSuccessStatusCode)
                {
                    isReady = true;
                    var jsonData = await response.Content.ReadFromJsonAsync<Response>();

                    Console.WriteLine("Fetch via FastApi from Python service");

                    foreach (var item in jsonData?.Data ?? new List<DataItem>())
                    {
                        Console.WriteLine($"ID: {item.Id}, Name: {item.Name ?? "Unknown"}, Value: {item.Value}");
                    }
                }
                else
                {
                    Console.WriteLine($"API request failed : {response}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Waiting for python producer... Error: {ex.Message}");
                await Task.Delay(3000);
            }
        }
    }
}

class Response
{
    public List<DataItem>? Data { get; set; }
}

class DataItem
{
    public int Id { get; set; }
    public string? Name { get; set; }
    public int Value { get; set; }
}