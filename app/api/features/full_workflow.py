from app.api.features.document_loaders import (
    generate_summary_from_img, 
    get_summary, 
    summarize_transcript_youtube_url
)
from app.api.features.schemas.schemas import RequestSchema, RequestSchemaWithFiles, SlidePresentationRequestArgs
from app.api.logger import setup_logger
from app.api.features.compile_chain_for_ppt import compile_chain

logger = setup_logger(__name__)

def full_workflow(args: RequestSchemaWithFiles):
  
    logger.info(f"File type uploaded successfully: {args.file_type}")
    logger.info("Generating the summary from the documents")

    if args.file_type == 'img':
        summary = generate_summary_from_img(args.file_url)
    elif args.file_type == 'youtube_url':
        summary = summarize_transcript_youtube_url(args.file_url)
    else:
        summary = get_summary(args.file_url, args.file_type)

    schema = RequestSchema(
        topic=args.request_args.topic,
        objective=args.request_args.objective,
        target_audience=args.request_args.target_audience,
        n_slides=args.request_args.n_slides,
        slide_breakdown=args.request_args.slide_breakdown,
        lang=args.request_args.lang,
        summary=summary
    )

    presentation = SlidePresentationRequestArgs(slide_schema=schema)

    logger.info(f"Summary generated successfully: {presentation.summary}")
    
    chain = compile_chain()
    
    logger.info("Generating the content for the PPT file")
    ppt_content = chain.invoke(presentation.validate_and_return())
    logger.info("PPT content generated successfully")

    return ppt_content