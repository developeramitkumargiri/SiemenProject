
FROM mcr.microsoft.com/dotnet/sdk:8.0
WORKDIR /app
COPY CSharpConsumer/CSharpConsumer.csproj /app/
RUN dotnet restore /app/CSharpConsumer.csproj
COPY CSharpConsumer/ /app/
RUN dotnet build --no-cache -o /app/build
EXPOSE 8080
CMD ["dotnet", "/app/build/CSharpConsumer.dll"]