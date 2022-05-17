docker build -t deribit-image .
docker run --network host -it --rm --name deribit-run deribit-image 
