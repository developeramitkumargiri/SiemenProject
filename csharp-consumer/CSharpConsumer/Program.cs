using System;
using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;

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
                //var response = await client.GetAsync("http://localhost:5000/data");
                var response = await client.GetAsync("http://fastapi-service:5000/data");
                if (response.IsSuccessStatusCode)
                {
                    isReady = true;
                    var jsonData = await response.Content.ReadFromJsonAsync<Response>();

                    foreach (var item in jsonData.data)
                    {
                        Console.WriteLine($"ID: {item[0]}, Name: {item[1]}, Value: {item[2]}");
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Waiting for Python Producer... Error: {ex.Message}");
                await Task.Delay(3000);
            }
        }
    }
}

class Response
{
    public object[][] data { get; set; }
}