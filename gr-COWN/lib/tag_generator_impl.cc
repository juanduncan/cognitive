/* -*- c++ -*- */
/* 
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "tag_generator_impl.h"

#include <iostream>
 using namespace std;

namespace gr {
  namespace COWN {

    tag_generator::sptr
    tag_generator::make()
    {
      return gnuradio::get_initial_sptr
        (new tag_generator_impl());
    }

    /*
     * The private constructor
     */
    tag_generator_impl::tag_generator_impl()
      : gr::sync_decimator("tag_generator",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(gr_complex))

              , 4)
    {
      set_history(600);
      count_errors =  0;
      counter = 0;
      set_output_multiple(4);


    }

    /*
     * Our virtual destructor.
     */
    tag_generator_impl::~tag_generator_impl()
    {
    }

    int
    tag_generator_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
                const int *in = (const int*) input_items[0];
                gr_complex *out = (gr_complex*)output_items[0];


                const float *in_float = (const float*) input_items[0];


                  // Do <+signal processing+>

                // int i = 0;
                // while (in[i]!= 0xFFFFFFFF){
                //     in++;
                // }

                int nitems_to_read = noutput_items*4;
                int i = 0;
                int o = 0;
                for(o=0; o< noutput_items; o++){

                  out[o]= gr_complex(  in_float[o*4+1]   ,  in_float[o*4+2]    );
                  i+=4;


                          // if(in[i+3] - in[i-1]!=80){
                          // count_errors++;
                          // cout << " COUNTER ERRROR  "<< dec << out[o] <<   "\tcount_errors="<< dec << count_errors <<  endl;

                          // cout << hex << in[i] << "\t" << in[i+1]<< " (" << in_float[i+1]<< ")" 
                          // << "\t" << in[i+2]  << "\t" << in[i+3] << dec << " ("<<  in[i+3]  << ")" 
                          // << "-" << hex<< in[i-1]<< dec << " ("<<  in[i+3]  << ")" <<  "\t" << in[i+3] - in[i-1]<<  endl;
                          

                          // }


                }


                                                        // if(  counter%250 == 1  ){
                                                            

                                                        //   char buffer[50];

                                                        //   int n;

                                                        //   // n=std::sprintf (buffer, "0x%f ", nitems_written(0) );
                                                     
                                                        //   cout<< "n_written(0)=  "<< nitems_written(0)  << "\t";


                                                        //   cout << hex 

                                                        //   << in[i] << " " 

                                                        //   << in[i+1]<< " I(" << in_float[i+1]<< ")" 

                                                        //   << in[i+2]<< " Q("<<  in_float[i+2]  << ")     " 

                                                        //   << "\t" << hex << in[i+3] << dec << " ("<<  in[i+3]  << ")" 

                                                        //   << "-" << hex<< in[i-1]<< dec << " ("<<  in[i+3]  << ")" <<  "\t" << in[i+3] - in[i-1]<<  endl;
                                                        // }

               counter++;

              return noutput_items;
    }

  } /* namespace COWN */
} /* namespace gr */

